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
![image](https://user-images.githubusercontent.com/61418085/235458839-2b147bef-7cb1-4662-bf47-93be04c55de6.png)


Once on the image upload page the user can upload an image of their ingredients and press upload.
![image](https://user-images.githubusercontent.com/61418085/235458905-172effdc-ab59-4bae-a83f-df3f88a4f1f8.png)

That will take the user to a page where they will be shown the image they uploaded with the bounding boxes on the objects detected and a table that contains the image and name of the ingredients detected aswell as the amount of that ingredient.
![image](https://user-images.githubusercontent.com/61418085/235460378-d0e3ece4-011b-4063-8cf8-6c39030aeafe.png)

From there the user can get recipes recommended to them that will use all the ingredients detected all atleast one ingredient. The following image shows what happens if you presse the "Recommend Recipes" button on that image that can be seen in the image above.
![image](https://user-images.githubusercontent.com/61418085/235460566-2c56521a-dde7-46fc-b633-db5444da0d16.png)
The user only gets provided with on recipes that uses all the ingredients in the image. The user still has the option to search for recipes that use atleast one ingredient.

![image](https://user-images.githubusercontent.com/61418085/235460732-874c5810-a818-4317-9904-8dbe2c612162.png)
It can be seen that in the alternative search there is more recipe available, this can be used to see what the user can make if they abuy another ingredient or two combinded with the ingredients they already have.



