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
    
    @app.route("/all_recipes", methods=["GET"])
    def all_recipes():
        recipes = Recipe.query.all()
        return render_template("recipes.html", recipes=recipes)
    
    @app.route("/viewRecipe/<int:id>", methods=["GET"])
    def viewRecipe(id):
        recipe = Recipe.query.get(id)
        instructions = Instruction.query.filter_by(Recipes_recipeID=id).order_by(Instruction.step_number.asc()).all()

        recipe_ingredients = (
            db.session.query(
                Ingredient.ingredientName,
                RecipeIngredient.quantity,
                Units.acronym
            )
            .join(RecipeIngredient, Ingredient.ingredientID == RecipeIngredient.Ingredients_ingredientID)
            .join(Units, RecipeIngredient.Units_unitID == Units.unitID)
            .filter(RecipeIngredient.Recipes_recipeID == recipe.recipeID)
            .all()
        )
        
        if recipe is None:
            return redirect("/")

        return render_template("recipePage.html", recipe=recipe, instructions=instructions, recipe_ingredients=recipe_ingredients)

    @app.route("/detect", methods=["GET", "POST"])
    def detect():
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

            results.render()
            now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
            img_savedirectory = f"static/detected_images/{now_time}.png"
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
            #Returns the recipe ID's as tuples
            recipesids = [recipeid[0] for recipeid in recipesids] #Takes the first element of each tuple and puts it in a list
            recipes = Recipe.query.filter(Recipe.recipeID.in_(recipesids)).all() # Queries the database and gets all the recipes using the recipes ID's

            option = 0

            if len(recipes) > 0:
                return render_template("recommended_recipes.html", recipes=recipes, option=option)
            else:
                return "No recipes found."
        else:
            return "No ingredients provided."
        
    @app.route("/recommend_recipes_alternative", methods=["GET", "POST"])
    def recommend_recipes_alternative():
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
                .having(func.count(distinct(RecipeIngredient.Ingredients_ingredientID)) >= 1)
            )

            recipesids = query.all() #Returns the recipe ID's as tuples
            recipesids = [recipeid[0] for recipeid in recipesids] #Takes the first element of each tuple and puts it in a list
            recipes = Recipe.query.filter(Recipe.recipeID.in_(recipesids)).all() # Queries the database and gets all the recipes using the recipes ID's

            option = 1
            if len(recipes) > 0:
                return render_template("recommended_recipes.html", recipes=recipes, option=option)
            else:
                return "No recipes found."
        else:
            return "No ingredients provided."

    return app