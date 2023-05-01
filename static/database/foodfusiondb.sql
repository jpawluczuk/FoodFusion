CREATE DATABASE  IF NOT EXISTS `foodfusiondb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `foodfusiondb`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: foodfusiondb
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.17-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `digitalfridge`
--

DROP TABLE IF EXISTS `digitalfridge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `digitalfridge` (
  `digitalFridgeID` int(11) NOT NULL AUTO_INCREMENT,
  `User_userID` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `Ingredient_ingredientID` int(11) NOT NULL,
  PRIMARY KEY (`digitalFridgeID`),
  KEY `fk_DigitalFridge_User1_idx` (`User_userID`),
  KEY `fk_DigitalFridge_Ingredient1_idx` (`Ingredient_ingredientID`),
  CONSTRAINT `fk_DigitalFridge_Ingredient1` FOREIGN KEY (`Ingredient_ingredientID`) REFERENCES `ingredient` (`ingredientID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_DigitalFridge_User1` FOREIGN KEY (`User_userID`) REFERENCES `user` (`userID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `digitalfridge`
--

LOCK TABLES `digitalfridge` WRITE;
/*!40000 ALTER TABLE `digitalfridge` DISABLE KEYS */;
/*!40000 ALTER TABLE `digitalfridge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredient` (
  `ingredientID` int(11) NOT NULL AUTO_INCREMENT,
  `ingredientName` varchar(120) NOT NULL,
  PRIMARY KEY (`ingredientID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (1,'chickenbreast'),(2,'Bell Pepper'),(3,'Onion'),(4,'Egg'),(5,'Butter');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instruction`
--

DROP TABLE IF EXISTS `instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instruction` (
  `instructionID` int(11) NOT NULL AUTO_INCREMENT,
  `step_number` int(11) NOT NULL,
  `description` varchar(200) NOT NULL,
  `Recipes_recipeID` int(11) NOT NULL,
  PRIMARY KEY (`instructionID`),
  KEY `fk_Instructions_Recipes1_idx` (`Recipes_recipeID`),
  CONSTRAINT `fk_Instructions_Recipes1` FOREIGN KEY (`Recipes_recipeID`) REFERENCES `recipe` (`recipeID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instruction`
--

LOCK TABLES `instruction` WRITE;
/*!40000 ALTER TABLE `instruction` DISABLE KEYS */;
INSERT INTO `instruction` VALUES (1,1,'Cut up the bell pepper small cubes',1),(2,2,'Crack the eggs into bowl and beat them untill the yolk and whites are combined',1),(3,3,'Heat the butter on the frying pan. Once the butter melts put the bell pepper into the frying pan',1),(4,4,'Stir fry the bell pepper for 1 minute',1),(5,5,'Once the bell pepper is soft add in the egg. Constantly stir the egg for about 45 seconds or until desired consistancy is met. Serve !',1),(6,2,'Place the chicken breast and vegetables  onto a piece of tin foil that is big enough to cover them from the top',2),(7,3,'Drizzle slightly with olive oil and your favourtie seasoning',2),(8,4,'Rub the spices into the chicken breast and vegetables',2),(9,5,'Fold the tin foil over everything and roll up the sides so the chciek breast and vegetables are sealed in a pocket',2),(10,6,'Place the pocket in the oven for 25 minutes, the chicken breast and vegetables will bake and steam in the pocket keeping all the flavour inside.',2),(11,1,'Preheat the oven to 180 degrees celcius',2),(12,7,'Take the pocket out of the oven, carefully open the pocket and check if the chicken breast is cooked. If not white on the inside, close the pocket and keep for an extra 5-10 minutes.',2),(13,2,'Chop the top of the bell peppers off and scoop out the insides',3),(14,3,'Place the bell pepper onto a baking tray covered with baking paper. If the bell pepper does not want to stay upright, take some tin foul and create a wal around the base of the bell peppers to keep it',3),(15,1,'Preheat the oven to 180 degrees celcius',3),(16,4,'Crack the eggs into the bell peppers and seasoning how you like',3),(17,5,'Place the bell pepper in the oven for 20 - 30 minutes or until the ',3),(18,6,'Once done, take out of the oven and enjoy!',3),(19,1,'Preheat the oven to 190 degrees celcius',4),(20,2,'Cut the vegetables into 1/4 inch thick strips',4),(21,3,'Place the vegetables on a baking tray covered with baking paper',4),(22,4,'Put the baking tray into the oven and bake for 20 - 30 minutes or until the edges start to blacken',4),(23,5,'Take out of the oven and enjoy!',4),(24,1,'Crack the eggs into a bowl and whisk until well the whites and yolk is well combines',5),(25,2,'Take the chicken breast and cut it into thin strips',5),(26,3,'Put a drizzle of olive oil into the a pan and wait until hot.',5),(27,4,'Stir fry the chicken strips for about 7 minutes',5),(28,5,'Put the chicken strips onto a plate and clean pan from the oil',5),(29,6,'Put 2 tbsp of butter on the the pan and wait until melted',5),(30,7,'Add the beaten eggs into the pan and mix so the egs don\'t burn.',5),(31,8,'Once the eggs start scrambling add back the chicken and stiur for another 20 seconds',5),(32,9,'Once done, place on a tortilla wrap, wrap it like a burrito and enjoy!',5),(33,1,'Cut the chicken breast into thin strips and place into a bowl',6),(34,2,'Cut the vegetables into 1/4 inch strips',6),(35,3,'Put 2 tbsp of olive onion into a drying pan and heat it up',6),(36,4,'Once the frying pan is hot, add the chicken, occationally stirring and cook for 5 miuntes.',6),(37,5,'Add in the vegetables, reduce to medium heat and cook for another 10 minutes',6),(38,7,'Once the vegetables turn translucent turn off the heat and enjoy!',6),(39,1,'Add 500ml of water into a pot and bring to a boil',7),(40,2,'Once water it boiling add in the eggs. For a soft boil, boil for 7 minutes.',7),(41,3,'When the time is up, take off the heat and rince under cold water until the shell in cool',7),(42,4,'This should make the egg yolk be soft while the whites are fully cooked, enjoy!',7);
/*!40000 ALTER TABLE `instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe` (
  `recipeID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `blurb` varchar(45) DEFAULT NULL,
  `prepTime` varchar(45) NOT NULL,
  `cookTime` varchar(45) NOT NULL,
  `image_url` varchar(45) NOT NULL,
  PRIMARY KEY (`recipeID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'Omlette with Bell Pepper','A delicious omlette cooked with bell peppers','5 minutes','5 minutes','#'),(2,'Oven Baked Chicken Breast','Oven baked chicken breast in a pocket ','20 minutes','30 minutes','#'),(3,'Egg Stuffed Bell Peppers','Delicious egg baked in peppers','10 minutes','30 minutes','#'),(4,'Roasted Peppers and Onions','Bell Peppers and Onion slow roasted ','15 minutes','25 minutes','# '),(5,'Chicken and Egg Wraps','Perfect quick breakfast ','5 minutes','15 minutes','#'),(6,'Chicken Fajitas','Chicken fajita filling ','15 minutes','15 minutes','#'),(7,'Soft Boiled Egg','Quick soft boiled egg','5 minutes','10 minutes','#');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_has_ingredients`
--

DROP TABLE IF EXISTS `recipes_has_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes_has_ingredients` (
  `Recipes_recipeID` int(11) NOT NULL,
  `Ingredients_ingredientID` int(11) NOT NULL,
  `quantity` varchar(10) NOT NULL,
  `Units_unitID` int(11) DEFAULT NULL,
  PRIMARY KEY (`Recipes_recipeID`,`Ingredients_ingredientID`),
  KEY `fk_Recipes_has_Ingredients_Ingredients1_idx` (`Ingredients_ingredientID`),
  KEY `fk_Recipes_has_Ingredients_Recipes1_idx` (`Recipes_recipeID`),
  KEY `fk_Recipes_has_Ingredients_Units1_idx` (`Units_unitID`),
  CONSTRAINT `fk_Recipes_has_Ingredients_Ingredients1` FOREIGN KEY (`Ingredients_ingredientID`) REFERENCES `ingredient` (`ingredientID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recipes_has_Ingredients_Recipes1` FOREIGN KEY (`Recipes_recipeID`) REFERENCES `recipe` (`recipeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recipes_has_Ingredients_Units1` FOREIGN KEY (`Units_unitID`) REFERENCES `units` (`unitID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_has_ingredients`
--

LOCK TABLES `recipes_has_ingredients` WRITE;
/*!40000 ALTER TABLE `recipes_has_ingredients` DISABLE KEYS */;
INSERT INTO `recipes_has_ingredients` VALUES (1,2,'1/4',5),(1,4,'3',8),(2,1,'1',6),(2,2,'1/2',5),(2,3,'1/2',5),(3,2,'3',8),(3,4,'3',8),(4,2,'2',5),(4,3,'2',5),(5,1,'1',5),(5,4,'3',8),(6,1,'1',5),(6,2,'1',5),(6,3,'1',5),(7,4,'3',8);
/*!40000 ALTER TABLE `recipes_has_ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoppinglist`
--

DROP TABLE IF EXISTS `shoppinglist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shoppinglist` (
  `shoppingListID` int(11) NOT NULL AUTO_INCREMENT,
  `listItem` varchar(120) NOT NULL,
  `User_userID` int(11) NOT NULL,
  PRIMARY KEY (`shoppingListID`),
  KEY `fk_ShoppingList_User1_idx` (`User_userID`),
  CONSTRAINT `fk_ShoppingList_User1` FOREIGN KEY (`User_userID`) REFERENCES `user` (`userID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppinglist`
--

LOCK TABLES `shoppinglist` WRITE;
/*!40000 ALTER TABLE `shoppinglist` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoppinglist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `units` (
  `unitID` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `acronym` varchar(45) NOT NULL,
  PRIMARY KEY (`unitID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
INSERT INTO `units` VALUES (1,'mililitre','ml'),(2,'litre','l'),(3,'tea spoon','tsp'),(4,'table spoon','tbsp'),(5,'cup','cup'),(6,'grams','g'),(7,'kilograms','kg'),(8,'Whole','Whole');
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(256) NOT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'John','Doe','johndoe@example.com','password');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'foodfusiondb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-01 15:30:22
