-- In a code editor file, write the SQL Code to create the UserLib table for the MySQL RDBMS. Carefully think of the data type for every column, whether a column can be left empty or not and whether additional constraints need to be defined.  Also carefully define your primary keys and foreign keys.

CREATE DATABASE Something;
use Something;
CREATE TABLE  UserLib(
UserID int(4) primary key, 
Username varchar(20) not null, 
Useremail varchar(15) not null, 
UserAddres varchar(25) not null);

-- Save your file, then copy and paste your code in the SQL area of phpMyAdmin (second tab) and run it by clicking on “Go”. You should see your successfully created table appearing in the list of tables on the left.

CREATE TABLE Librarian(
StaffID int primary key, 
LibFullname varchar(20) not null, 
Libaddress varchar(25) 
LibTelNo bigint(10));

-- In the same code editor file, write the SQL Code to create the Publisher  table for the MySQL RDBMS. Carefully think of the data type for every column, whether a column can be left empty or not and whether additional constraints need to be defined.  Also carefully define your primary keys and foreign keys.

CREATE TABLE Publisher( 
PubID int primary key,
PubName varchar(20) not null,
PubAddress varchar(25) not null,
PubLicenseNo int not null,
StaffID int,
);
ALTER TABLE Publisher
ADD FOREIGN KEY(StaffID) REFERENCES Librarian(StaffID)

-- In the code editor file, write the SQL Code to create the Book table for the MySQL RDBMS. Carefully think of the data type for every column, whether a column can be left empty or not and whether additional constraints need to be defined.  Also carefully define your primary keys and foreign keys.

CREATE TABLE Book(
ISBN int primary key,
BookName varchar(10) not null,
BookAuthor varchar(10) not null,
YearOfPub date not null,
PubID int,
StaffID int,
UserID int);
ALTER TABLE Book
ADD FOREIGN KEY(PubID) REFERENCES Publisher(PubID);
ADD FOREIGN KEY(StaffID) REFERENCES Librarian(StaffID);
ADD FOREIGN KEY(UserID) REFERENCES UserLib(UserID);

-- In a code editor file, write the SQL Code to create the Doctor table for the MySQL RDBMS. Carefully think of the data type for every column, whether a column can be left empty or not and whether additional constraints need to de defined.  Also carefully define your primary keys and foreign keys.

CREATE DATABASE MedicOrg;
use MedicOrg;
CREATE TABLE Doctor(
docId int primary key,
docFullName varchar(25) not null,
JoinDate date not null,
docSpeciality varchar(10) not null,
hospCode int);
ALTER TABLE Doctor
ADD FOREIGN KEY(hospCode) REFERENCES Hospital(PubID);

-- In the code editor file, write the SQL Code to create the Patient table for the MySQL RDBMS. Carefully think of the data type for every column, whether a column can be left empty or not and whether additional constraints need to de defined.  Also carefully define your primary keys and foreign keys.

CREATE TABLE Patient(
patientNb int primary key,
pFullName varchar(20) not null,
pDOB date not null,
pHeight varchar(3) not null,
docId int,
pWeight varchar(3) not null);

ALTER TABLE Patient
ADD FOREIGN KEY(docID) REFERENCES Doctor(docID);

-- In the same code editor file, write the SQL Code to create the Hospital table for the MySQL RDBMS. Carefully think of the data type for every column, whether a column can be left empty or not and whether additional constraints need to de defined.  Also carefully define your primary keys and foreign keys.

CREATE TABLE Hospital(
hospCode int primary key,
hAdderess varchar(20) not null,
hPostCode bigint(10) not null,
hCity varchar(10) not null);
