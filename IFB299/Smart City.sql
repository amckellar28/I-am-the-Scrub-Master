#Create Database
CREATE DATABASE IF NOT EXISTS SmartCity;

Use SmartCity;

#Create User Table
CREATE TABLE User (UserID INT(11) NOT NULL AUTO_INCREMENT,
Username varchar(30) NOT NULL,
firstname varchar(45) NOT NULL,
lastname varchar(45) NOT NULL,
Gender enum('female', 'male') DEFAULT NULL,
DOB DATE DEFAULT NULL,
Email varchar(320) NOT NULL,
streetNumber varchar(15) DEFAULT NULL,
streetName varchar(30) DEFAULT NULL,
city varchar(45) DEFAULT NULL,
postcode char(4) DEFAULT NULL,
Phonenumber char(10) DEFAULT NULL,
PRIMARY KEY (UserID)
) CHARACTER SET utf8;

#Test Data
INSERT INTO User(Username, firstname, lastname, Gender, DOB, Email)
VALUES ('Johnny12', 'Johnny', 'Smith', 'male', '1999-03-12', 'johnnyboy@gmail.com');

INSERT INTO User(Username, firstname, lastname, Gender, DOB, Email, streetNumber, streetName, city, postcode, Phonenumber)
VALUES ('JaneIT', 'Jane', 'Roth', 'female', '1995-06-22', 'janegirl@gmail.com', '60', 'Tribune Street', 'Brisbane', '4101', '0463782665'),
	   ('Ronnie', 'Ron', 'Tron', 'male', '2000-07-07', 'ronnietron@hotmail.com', '24', 'Mary Street', 'Perth', '1111', '0467382117');

#Create Information Table
CREATE TABLE Information (InfoID INT(11) NOT NULL auto_increment,
InfoName varchar(250) NOT NULL,
CategoryType enum('Colleges', 'Libraries', 'Industries', 'Hotels', 'City Information') NOT NULL,
Phonenumber char(10) NOT NULL,
streetNumber varchar(15) NOT NULL,
streetName varchar(30) NOT NULL,
suburb varchar(45) NOT NULL,
postcode char(4) NOT NULL,
Email varchar(320) NOT NULL,
departments varchar (30) DEFAULT NULL,
industryType varchar (30) DEFAULT NULL,
PRIMARY KEY (InfoID)
) CHARACTER SET utf8;

#Test Data
INSERT INTO Information(InfoName, CategoryType, Phonenumber, streetNumber, streetName, suburb, postcode, Email)
VALUES ('Queensland University of Technology', 'Colleges', '0731382000', '2', 'George Street', 'Brisbane City', '4000', 'askqut@qut.edu.au'),
	   ('Treasury Casino & Hotel', 'Hotels', '0733068888', '130', 'William Street', 'Brisbane City', '4000', 'brtcswitchboard@star.com.au ');
       
INSERT INTO Information(InfoName, CategoryType, Phonenumber, streetNumber, streetName, suburb, postcode, Email, industryType)
VALUES ('The Myer Centre', 'Industries', '0732236900', '91', 'Queen Street', 'Brisbane City', '4000', 'Brisbane.MyerCentre@vicinity.com.au', 'Retail');

Select * from information;
Select * from User;