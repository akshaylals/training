USE employee_db

--create table 
CREATE TABLE emp_details(
	id INT IDENTITY PRIMARY KEY,
	name VARCHAR(50),
	age SMALLINT,
	location VARCHAR(50)
);

--add dob
ALTER TABLE emp_details ADD dob DATE;

--describe table 
EXEC sp_help emp_details;

--insert data into table 
INSERT INTO emp_details (name, age, location, dob)
VALUES ('Tom', 2, 'USA', '2019-10-20'),
('Jerry', 1, 'USA', '2019-03-20'),
('Mickey', 3, 'USA', '2018-10-22');

SELECT * FROM emp_details;

--update data in a table
UPDATE emp_details
SET name = 'donald'
WHERE name = 'Tom';


--delete data from table
DELETE FROM emp_details
WHERE name = 'donald';


--delete a table
DROP TABLE emp_details;

--to generate this from UI
--right click table -> script table as
USE [employee_db]
GO

INSERT INTO [dbo].[emp_details]
           ([name]
           ,[age]
           ,[location]
           ,[dob])
     VALUES
           (<name, varchar(50),>
           ,<age, smallint,>
           ,<location, varchar(50),>
           ,<dob, date,>)
GO




USE Northwind;

SELECT * FROM Customers;

--minimum
SELECT MIN(unitprice) AS 'Min Product Price' FROM Products;

--maximum
SELECT MAX(unitprice) AS 'Max Product Price' FROM Products;

--average
SELECT AVG(unitprice) FROM Products

--using aggregate function as a subquery
SELECT productid, productname, unitprice
FROM Products
WHERE UnitPrice = (SELECT MIN(unitprice) FROM Products);

SELECT productid, productname, unitprice
FROM Products
WHERE UnitPrice = (SELECT MAX(unitprice) FROM Products);

SELECT productid, productname, unitprice
FROM Products
WHERE UnitPrice > (SELECT AVG(unitprice) FROM Products);

SELECT productid, productname, unitprice
FROM Products
WHERE UnitPrice < (SELECT AVG(unitprice) FROM Products);


-- get list of tables in selected database
SELECT name FROM sys.tables;


--sum fn
SELECT SUM(unitsinstock) AS 'Total Stock'
FROM Products;

SELECT SUM(unitsinstock) AS 'Total Stock'
FROM Products
WHERE Discontinued = 1;


--count fn
SELECT COUNT(ProductID) AS 'Products Count'
FROM Products;

SELECT COUNT(ProductID) AS 'Products Count'
FROM Products
WHERE Discontinued = 1;


--clauses in SQL
--DISTINCT clause
SELECT DISTINCT City FROM Customers;

SELECT DISTINCT City, Region FROM Customers;

SELECT DISTINCT City, Region FROM Customers
WHERE Country = 'UK';

--GROUP BY
SELECT COUNT(customerid) AS 'No of Customers', Country
FROM Customers
GROUP BY Country;

SELECT COUNT(customerid) AS 'No of Customers', Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(customerid);