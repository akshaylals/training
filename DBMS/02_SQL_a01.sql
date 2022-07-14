--create database
CREATE DATABASE hospital_db;

USE hospital_db;

--create table
CREATE TABLE patient(
	record_no INT IDENTITY PRIMARY KEY,
	name VARCHAR(50),
	phone INT,
	gender VARCHAR(2),
	age SMALLINT,
	location VARCHAR(50)
);


--change phone to BIGINT
ALTER TABLE patient ALTER COLUMN phone BIGINT;

--insert data
INSERT INTO patient(name, phone, gender, age, location)
VALUES ('Tom', 1234567890, 'M', 5, 'USA'),
('Jerry', 1234567890, 'M', 4, 'USA'),
('Daisy', 4567123890, 'F', 5, 'USA'),
('Donald', 6789012345, 'M', 5, 'USA');


--update data in table
UPDATE patient
SET phone = 0987654321
WHERE name = 'Jerry';


--delete data from table
DELETE FROM patient
WHERE name = 'Tom';

SELECT * FROM patient;