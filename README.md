# FoodFusion

## Project Description
FoodFusion is a object betection based web application that provides users with recipes based on the ingredients that they have. The user uploads an image of their ingredients and the applicaiton provides them with delicious recipes.

## Requirements
- Python 3.9 or above
- pip
- xampp
  
## Installation Instructions
(Taking into account that you have the repository on your local machine)
1. Run xampp and start the Apache and MySQL modules
2. Import the database from the static/database folder, the file is called foodfusion.sql.
3. Open the project in your IDE (For the project I used VS Code)
4. Open the terminal
5. Run the following command to create a virtual environment
``` python -m venv venv``` This will create a folder called venv in the projects directory
6.  To active the virtual environment you can do one of the following:
    - Change the Python interpreter in the IDE to the one in the venv folder
    - Run this command to activate the virtual environment
    ``` venv\Scripts\Activate.ps1```
7. Run the follwing command to install the required packages (this can take a while):
``` pip install -r requirements.txt```
8. Once the packages have been installed you can run the application by running the following command:
``` flask --app app run```
9. To view the application after it is running, open a browser and go to the following url:
``` http://localhost:5000/```

## Usage
The project as of right now has one function and that is to provide a recipe to the user based on the ingredients that they have. 

The user can go to the image upload page via the "Detect" button on the nav bar or the "Detect Ingredients" button on the home page. 

Once on the image upload page the user can upload an image of their ingredients and press upload. That will take the user and display 
