from app import db

class Ingredient(db.Model):
    __tablename__ = "ingredient"
    ingredientID = db.Column(db.Integer, primary_key=True)
    ingredientName = db.Column(db.String(120), nullable=False)