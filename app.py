import io
import os
import datetime
from flask import Flask, render_template, request, redirect
from PIL import Image

import torch    # pip install torch torchvision

app = Flask(__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

model = torch.hub.load('ultralytics/yolov5', 'custom', path="D:\Forth_Year_College_Work\FYP\FoodFusion/best.pt")  # force_reload = recache latest code

@app.route("/")
def index():
    return render_template("index.html")

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
            results = model(img, size=640) # reduce size=320 for faster inference

            ingredients = set()
            for r in results.pandas().xyxy[0].to_dict(orient="records"):
                ingredients.add(r["name"])

            ingredients = sorted(list(ingredients))

            return ingredients
            # return results.pandas().xyxy[0].to_json(orient="records")

    return render_template("index.html")

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