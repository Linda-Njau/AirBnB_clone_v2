--this script prepares a MYSQL server for project
--this creates the database hbnb_test_db
CREATE DATABASE IF NOT EXIST hbnb_test_db;
--creates a user hbnb_test @localhost and sets a password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--this grants the user hbnb_test select privilege for the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
--this grants the user hbnb_test all privileges to the hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;