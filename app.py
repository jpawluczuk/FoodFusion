import io
import os
import datetime
from flask import Flask, render_template, request, redirect, jsonify, session
from sqlalchemy import func, case, and_, distinct
from PIL import Image
from database import *

import torch    # pip install torch torchvision

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/foodfusiondb"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "dev"
    db.init_app(app)
    model = torch.hub.load('ultralytics/yolov5', 'custom', path="D:\Forth_Year_College_Work\FYP\FoodFusion/static/best.pt")  # force_reload = recache latest code
    
    DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            return redirect("/")

        return render_template("login.html")

    @app.route("/detect", methods=["GET", "POST"])
    def predict_test():
        if request.method == "POST":
            if "file" not in request.files:
                return redirect(request.url)
            file = request.files["file"]
            if not file:
                return

        if request.files.get("file"):
            image_file = request.files["file"]
            image_bytes = image_file.read()
            img = Image.open(io.BytesIO(image_bytes))

            model.conf = 0.70
            results = model(img, size=640) 

            ingredients_dict = {}
            for r in results.pandas().xyxy[0].to_dict(orient="records"):
                ingredient_name = r["name"]
                if ingredient_name in ingredients_dict:
                    ingredients_dict[ingredient_name] += 1
                else:
                    ingredients_dict[ingredient_name] = 1

            results.render()  # updates results.imgs with boxes and labels
            now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
            img_savedirectory = f"static/{now_time}.png"
            Image.fromarray(results.ims[0]).save(img_savedirectory)
            session['ingredients'] = ingredients_dict

            return render_template("results.html", ingredients=ingredients_dict, img_name=img_savedirectory)
        
        return render_template("detect.html")

    @app.route("/recommend_recipes", methods=["GET", "POST"])
    def recommend_recipes():
        ingredients_dict = session.get('ingredients')
        if ingredients_dict:
            ingredient_names = list(ingredients_dict.keys())
            ingredient_names = [x for x in ingredient_names if not isinstance(x, int)]
            print(ingredient_names)

            results = (
                db.session.query(Ingredient.ingredientID)
                .filter(Ingredient.ingredientName.in_(ingredient_names))
                .all()
            )

            ingredient_ids = [result[0] for result in results]
            print(ingredient_ids)

            query = (
                db.session.query(Recipe.recipeID)
                .join(RecipeIngredient, Recipe.recipeID == RecipeIngredient.Recipes_recipeID)
                .filter(RecipeIngredient.Ingredients_ingredientID.in_(ingredient_ids))
                .group_by(Recipe.recipeID)
                .having(and_(*[func.count(distinct(RecipeIngredient.Ingredients_ingredientID)) == len(ingredient_ids)]))
            )

            recipesids = query.all()
            recipesids = [recipeid[0] for recipeid in recipesids]
            print(recipesids)
            recipes = db.session.execute(db.select(Recipe).filter(Recipe.recipeID.in_(recipesids))).fetchall()
            print(recipes)

            if len(recipes) > 0:
                return render_template("recipePage.html", recipes=recipes)
            else:
                return "No recipes found."
        else:
            return "No ingredients provided."


    #@app.route("/test")
    #def test():
    #    ingredients = Ingredient.query.all()
    #    result = [{"ingredientID": ingredient.ingredientID, "ingredientName": ingredient.ingredientName} for ingredient in ingredients]
    #    return jsonify(result)

    #@app.route("/test-two")
    #def testtwo():
    #    ingredients = Ingredient.query.all()
    #    return render_template("test.html", ingredients=ingredients)

    #@app.route("/ts", methods=["GET", "POST"])
    #def predict():
    #    if request.method == "POST":
    #        if "file" not in request.files:
    #            return redirect(request.url)
    #        file = request.files["file"]
    #        if not file:
    #            return
    #
    #       img_bytes = file.read()
    #        img = Image.open(io.BytesIO(img_bytes))
    #        results = model([img])
    #
    #        results.render()  # updates results.imgs with boxes and labels
    #        now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
    #        img_savename = f"static/{now_time}.png"
    #        Image.fromarray(results.ims[0]).save(img_savename)
    #        return redirect(img_savename)
    #
    #    return render_template("index.html")
    return app