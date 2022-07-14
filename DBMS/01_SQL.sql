--To create a database
CREATE DATABASE employee_db

--List all databases in the server
SELECT name from master.sys.databases

--List all databases in the server order by name
SELECT name from master.sys.databases ORDER BY name

--Select the database
USE employee_db;

--Create database backup 
BACKUP DATABASE employee_db TO DISK = 'C:\database\employee_db.bak'

--Create database backup differential backup
BACKUP DATABASE employee_db TO DISK = 'C:\database\employee_db.bak'
WITH DIFFERENTIAL

USE master
--delete the database
DROP DATABASE employee_db

--restore database from backup
RESTORE DATABASE employee_db 
FROM DISK = 'C:\database\employee_db.bak'
WITH REPLACE

USE employee_db
--find the default schema of the current database
SELECT SCHEMA_NAME()

--creating schema
CREATE SCHEMA myschema1 

--creating schema by explicitly specifying the user
CREATE SCHEMA myschema1 AUTHORIZATION dbo

--create table and placing it under myschema1
CREATE TABLE myschema1.table1(
	ID INT,
	FirstName NVARCHAR(50) NOT NULL,
	LastName NVARCHAR(50) NOT NULL
)

CREATE TABLE EmployeeMaster(
	ID INT,
	FirstName NVARCHAR(50) NOT NULL,
	LastName NVARCHAR(50) NOT NULL
)

--alter created schema 
ALTER SCHEMA myschema1 TRANSFER OBJECT::dbo.EmployeeMaster

--change ownership of schema to dbo
ALTER AUTHORIZATION ON SCHEMA :: myschema1 TO dbo


ALTER SCHEMA dbo TRANSFER OBJECT::myschema1.EmployeeMaster
ALTER SCHEMA dbo TRANSFER OBJECT::myschema1.table1
--remove the schema from the database
DROP SCHEMA myschema1
