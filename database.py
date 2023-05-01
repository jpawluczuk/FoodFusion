from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(45), nullable=False)
    lastName = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256), nullable=False)

class Ingredient(db.Model):
    __tablename__ = "ingredient"
    ingredientID = db.Column(db.Integer, primary_key=True)
    ingredientName = db.Column(db.String(120), nullable=False)

class DigitalFridge(db.Model):
    __tablename__ = "digitalfridge"
    digitalFridgeID = db.Column(db.Integer, primary_key=True)
    User_userID = db.Column(db.Integer, db.ForeignKey("user.userID"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    Ingredient_ingredientID = db.Column(db.Integer, db.ForeignKey("ingredient.ingredientID"), nullable=False)

class Instruction(db.Model):
    __tablename__ = "instruction"
    instructionID = db.Column(db.Integer, primary_key=True)
    step_number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    Recipes_recipeID = db.Column(db.Integer, db.ForeignKey("recipe.recipeID"), nullable=False)

class Recipe(db.Model):
    __tablename__ = "recipe"
    recipeID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    blurb = db.Column(db.String(45), nullable=True)
    prepTime = db.Column(db.String(45), nullable=False)
    cookTime = db.Column(db.String(45), nullable=False)
    image_url = db.Column(db.String(45), nullable=False)

class RecipeIngredient(db.Model):
    __tablename__ = "recipes_has_ingredients"
    Recipes_recipeID = db.Column(db.Integer, db.ForeignKey("recipe.recipeID"), primary_key=True, nullable=False)
    Ingredients_ingredientID = db.Column(db.Integer, db.ForeignKey("ingredient.ingredientID"), primary_key=True, nullable=False)
    quantity = db.Column(db.String(10), nullable=False)
    Units_unitID = db.Column(db.Integer, db.ForeignKey("units.unitID"), nullable=False)

class Units(db.Model):
    __tablename__ = "units"
    unitID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    acronym = db.Column(db.String(45), nullable=False)

class ShoppingList(db.Model):
    __tablename__ = "shoppinglist"
    shoppinglistID = db.Column(db.Integer, primary_key=True)
    listItem = db.Column(db.String(120), nullable=False)
    User_userID = db.Column(db.Integer, db.ForeignKey("user.userID"), nullable=False)
