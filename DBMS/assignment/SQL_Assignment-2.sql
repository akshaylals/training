--A

USE employee_db;

--Create Department table
CREATE TABLE Department(
	Deptno DECIMAL(2) NOT NULL,
	Deptname VARCHAR(50) UNIQUE,
	Location VARCHAR(50),
	CONSTRAINT department_pk
		PRIMARY KEY(Deptno)
)

--Create Employee table
CREATE TABLE Employee(
	Empno DECIMAL(3) PRIMARY KEY,
	ManagerID DECIMAL(3),
	FirstName VARCHAR(20) NOT NULL,
	LastName VARCHAR(20),
	UserID VARCHAR(20),
	deptno DECIMAL(2) NOT NULL,
	salary DECIMAL(5),
	Commission DECIMAL(3),
	JoiningDate DATE,
	Designation VARCHAR(25),
	CONSTRAINT fk_department
		FOREIGN KEY (deptno)
		REFERENCES Department(Deptno)
		ON DELETE CASCADE
);

--Add HRA field to Employee
ALTER TABLE Employee
ADD HRA DECIMAL(5, 2);

--Add PF field to Employee
ALTER TABLE Employee
ADD PF DECIMAL(5, 2) CHECK(PF <= 5000);

--Insert values into department
INSERT INTO Department(Deptno, Deptname, Location) VALUES
	(1, 'Development', 'TVM'),
	(2, 'Testing', 'KOC');
	
--Insert values into employee
INSERT INTO Employee(Empno, ManagerID, FirstName, LastName, UserID, deptno, salary, Commission, JoiningDate, Designation) VALUES
	(123, 102, 'Albert', 'Einstein', 'einstein', 2, 26000, 30, '03/01/2020', 'tester'),
	(111, 101, 'Nicolas', 'Tesla', 'nicolastesla', 1, 27000, 20, '02/07/1990', 'developer'),
	(354, 101, 'Spider', 'man', 'spiderman', 1, 12000, 10, '12/07/2022', 'developer'),
	(135, 104, 'James', 'Bond', 'jamesbond', 2, 14000, 5, '06/10/2021', 'tester'),
	(321, 102, 'Jack', 'Sparrow', 'jacksparrow', 1, 20000, 15, '01/12/2020', 'developer'),
	(213, 103, 'John', 'McClane', 'john', 2, 11000, 5, '03/11/2021', 'tester');

--list all details of employees sorted by name
SELECT * FROM Employee
	ORDER BY FirstName;
	
--list all details of employees sorted by salary in descending order
SELECT * FROM Employee
	ORDER BY salary DESC;

--list all details of employees whose name starts with a and contains e and ends with t
SELECT * FROM Employee
	WHERE FirstName LIKE 'A%e%t';

--list all details of employees whose joining date is > 01-jan-1998
SELECT * FROM Employee
	WHERE salary > 25000 
	AND JoiningDate > '01/01/1998';


--B
CREATE DATABASE Sales_db;
USE Sales_db;

CREATE TABLE Customer(
	Custno DECIMAL(3) NOT NULL PRIMARY KEY,
	Custname VARCHAR(20),
	Address VARCHAR(40)
);

CREATE TABLE Orders(
	orderno DECIMAL(3) NOT NULL PRIMARY KEY,
	custno DECIMAL(3) NOT NULL,
	orderdate DATE,
	CONSTRAINT fk_customer
		FOREIGN KEY (custno)
		REFERENCES Customer(Custno)
);

CREATE TABLE OrderItem(
	ItemID DECIMAL(3) NOT NULL PRIMARY KEY,
	OrderNo DECIMAL(3) NOT NULL,
	ItemName VARCHAR(20),
	Quantity DECIMAL(2)
	CONSTRAINT fk_orders
		FOREIGN KEY (OrderNo)
		REFERENCES Orders(orderno)
);