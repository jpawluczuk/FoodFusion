import io
import os
import datetime
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
from database import db, Ingredient

import torch    # pip install torch torchvision

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/foodfusiondb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

model = torch.hub.load('ultralytics/yolov5', 'custom', path="D:\Forth_Year_College_Work\FYP\FoodFusion/best.pt")  # force_reload = recache latest code

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

        return render_template("results.html", ingredients=ingredients_dict, img_name=img_savedirectory)
    
    return render_template("detect.html")

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