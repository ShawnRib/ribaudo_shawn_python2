import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd = "SQL5Data",

)

my_cursor = mydb.cursor()
#uncomment below if you want to create a database
my_cursor. execute("DROP DATABASE puppies;")
my_cursor. execute("CREATE DATABASE puppies;")
#my_cursor. execute("USE puppies;") ????????????????

my_cursor. execute("CREATE TABLE `puppies`.`puppies` (`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NULL,`color_fur` VARCHAR(45) NULL, `owner` INT NULL,PRIMARY KEY (`id`));")
my_cursor. execute("CREATE TABLE `puppies`.`owners` (`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NULL, `puppy_id` INT NULL,PRIMARY KEY (`id`));")

'''
CREATE TABLE `puppies`.`puppies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `owner` INT NULL,
  PRIMARY KEY (`id`));
  
  CREATE TABLE `puppies`.`owners` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `owner` INT NULL,
  PRIMARY KEY (`id`));
'''
#my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#my_cursor. execute("DROP DATABASE owners")
#my_cursor. execute("CREATE DATABASE owners")
#insert table!!!!

#add dummy information

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
