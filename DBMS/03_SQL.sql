USE Northwind

--WHERE =
SELECT CompanyName, City, Country
	FROM Suppliers
	WHERE Country = 'USA'
	ORDER BY CompanyName;

--WHERE BETWEEN
SELECT * FROM Employees
	WHERE EmployeeID BETWEEN 1 AND 5;

--WHERE IN
SELECT * FROM Employees
	WHERE EmployeeID IN (1, 2, 3);

--WHERE LIKE 
SELECT * FROM Employees
	WHERE FirstName LIKE 'Robert';

--ORDER BY 
SELECT FirstName, BirthDate FROM Employees
	ORDER BY BirthDate DESC;
	
SELECT FirstName, BirthDate FROM Employees
	ORDER BY BirthDate DESC,
	FirstName ASC;

--HAVING
--HAVING can be used with aggregate functions
SELECT ProductName, UnitPrice FROM Products
	GROUP BY ProductName, UnitPrice
	HAVING AVG(UnitPrice)>20;

--SELECT Clause
SELECT * FROM Products;

SELECT ProductName, UnitPrice FROM Products;

SELECT 1 + 1;

SELECT CONCAT(FirstName, ' ', LastName) AS Fullname
FROM Employees;

SELECT ProductName, UnitPrice*UnitsInStock AS Cost FROM Products;


USE employee_db;
CREATE TABLE EmployeeMaster(
	Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
);

INSERT INTO EmployeeMaster(EmployeeCode, EmployeeName, DepartmentCode, LocationCode, Salary)
VALUES
('E0001', 'Hulk', 'IT', 'TVM', 4000),
('E0002', 'Spiderman', 'IT', 'TVM', 4000),
('E0003', 'Ironman', 'QA', 'KLM', 3000),
('E0004', 'Superman', 'QA', 'KLM', 3000),
('E0005', 'Batman', 'HR', 'TVM', 5000),
('E0006', 'Raju', 'HR', 'KTM', 5000),
('E0007', 'Radha', 'HR', 'KTM', 5000);

--GROUPING SETS Clause
SELECT EmployeeCode, EmployeeName, DepartmentCode, LocationCode, SUM(salary) TotalCost
FROM EmployeeMaster
GROUP BY
	GROUPING SETS(
		(EmployeeCode, EmployeeName, DepartmentCode, LocationCode),
		(DepartmentCode),
		(LocationCode),
		()
	);


--Basic operators in SQL
SELECT * FROM EmployeeMaster WHERE Salary = 3000;
SELECT * FROM EmployeeMaster WHERE Salary < 3000;
SELECT * FROM EmployeeMaster WHERE Salary <= 3000;
SELECT * FROM EmployeeMaster WHERE Salary > 3000;
SELECT * FROM EmployeeMaster WHERE Salary >= 3000;
SELECT * FROM EmployeeMaster WHERE Salary !> 3000;
SELECT * FROM EmployeeMaster WHERE Salary !< 3000;

--IN and NOT operators
SELECT * FROM EmployeeMaster
	WHERE Salary IN (3000, 5000);

SELECT * FROM EmployeeMaster
	WHERE EmployeeName IN ('Raju', 'Radha');

SELECT * FROM EmployeeMaster 
	WHERE EmployeeName NOT IN ('Raju', 'Radha');

--BETWEEN, NOT, NULL
SELECT * FROM EmployeeMaster
	WHERE Salary BETWEEN 3000 AND 5000;

SELECT * FROM EmployeeMaster
	WHERE Salary IS NOT NULL;

SELECT * FROM EmployeeMaster
	WHERE Salary IS NULL;

--LIKE
SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE 'super';

SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE 'sup%';
	
SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE '%man';
	
SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE '%ra%';
	
SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE 'su[pj]erman%';
	
SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE 'ra[nj]u%';

SELECT * FROM EmployeeMaster 
	WHERE EmployeeName LIKE 'ra[^nj]u%';

SELECT * FROM EmployeeMaster 
	WHERE EmployeeName NOT LIKE 'raj%';

--EXISTS operator
SELECT * FROM EmployeeMaster WHERE EXISTS
	(SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Superman');
	


CREATE TABLE EmployeeMaster2(
	Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
);

INSERT INTO EmployeeMaster2(EmployeeCode, EmployeeName, DepartmentCode, LocationCode, Salary)
VALUES
('E0001', 'Arun', 'IT', 'TVM', 5000),
('E0002', 'Varun', 'IT', 'TVM', 4000),
('E0003', 'Kiran', 'QA', 'KLM', 3050),
('E0004', 'Superman', 'QA', 'KLM', 3000),
('E0005', 'Midhun', 'HR', 'TVM', 1000),
('E0006', 'Singh', 'HR', 'KTM', 6000),
('E0007', 'Jyothi', 'HR', 'KTM', 4000);

--UNION operator
SELECT * FROM EmployeeMaster
UNION
SELECT * FROM EmployeeMaster2;

SELECT * FROM EmployeeMaster
UNION ALL
SELECT * FROM EmployeeMaster2;

SELECT EmployeeName, Salary FROM EmployeeMaster
	WHERE Salary > 3000
UNION
SELECT EmployeeName, Salary FROM EmployeeMaster2;

--INTERSECT operator
SELECT * FROM EmployeeMaster
INTERSECT
SELECT * FROM EmployeeMaster2;

SELECT EmployeeName, Salary FROM EmployeeMaster
	WHERE Salary > 2000
INTERSECT
SELECT EmployeeName, Salary FROM EmployeeMaster2;


--SQL Server datatypes
CREATE TABLE data_types_eg(
	bit_col BIT,
	char_col CHAR(3),
	date_col DATE,
	date_time_col DATETIME2(3),
	date_time_offset_col DATETIMEOFFSET(2),
	dec_col DECIMAL(4, 2),
	num_col NUMERIC(4, 2),
	bitint_col BIGINT,
	int_col INT,
	smallint_col SMALLINT,
	tinyint_col TINYINT,
	nchar_col NCHAR(10),
	nvarchar_col NVARCHAR(10),
	time_col TIME(0),
	varchar_col VARCHAR(10)
);

INSERT INTO data_types_eg VALUES(
	1,
	'ABC',
	'2020-07-08',
	'2020-07-08 12:47:50',
	'2020-07-08 12:47:50 +05:30',
	10.23,
	10.36,
	695445514873981372,
	1879878979,
	32000,
	250,
	N'你好',
	N'你好',
	'2:47:50',
	'Hello'
);

SELECT * FROM data_types_eg;


--Constraints
--PRIMARY KEY
CREATE TABLE usage_logs(
	logid INT NOT NULL IDENTITY PRIMARY KEY,
	message CHAR(255) NOT NULL
);

--Setup PRIMARY KEY for multiple columns
CREATE TABLE customer_orders(
	OrderID INT NOT NULL,
	ProductID INT NOT NULL,
	UnitPrice INT,
	PRIMARY KEY (OrderID, ProductID)
);


--Altering table to include primary key later
CREATE TABLE cricketers(
	cricketer_id INT NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	salary MONEY
);

ALTER TABLE cricketers ADD CONSTRAINT
crick_id_pk PRIMARY KEY (cricketer_id);

--To view PRIMARY KEY ID
EXEC sp_help cricketers;

--Disable PRIMARY KEY
ALTER INDEX crick_id_pk ON cricketers DISABLE;

--Enable PRIMARY KEY
ALTER INDEX crick_id_pk ON cricketers REBUILD;

--Drop/delete PRIMARY KEY
ALTER TABLE cricketers DROP CONSTRAINT crick_id_pk;


--Create FOREIGN KEY
CREATE TABLE myproducts(
	product_id INT NOT NULL IDENTITY,
	product_name VARCHAR(50) NOT NULL,
	category VARCHAR(25),
	CONSTRAINT myproducts_pk PRIMARY KEY(product_id, product_name)
);

CREATE TABLE myinventory(
	inventory_id INT PRIMARY KEY,
	product_id INT NOT NULL,
	product_name VARCHAR(50) NOT NULL,
	quantity INT,
	min_level INT,
	max_level INT,
	CONSTRAINT fk_myinventory
		FOREIGN KEY (product_id, product_name)
		REFERENCES myproducts(product_id, product_name)
);

--Disable FOREIGN KEY
ALTER TABLE myinventory
	CHECK CONSTRAINT fk_myinventory

--Enable FOREIGN KEY
ALTER TABLE myinventory
	NOCHECK CONSTRAINT fk_myinventory

--Drop FOREIGN KEY
ALTER TABLE myinventory
	DROP CONSTRAINT fk_myinventory;


--NOT NULL CONSTRAINT
--inserts successfully
INSERT INTO usage_logs VALUES
('test')

--inserts successfully
INSERT INTO usage_logs VALUES
('')

--insert fails
INSERT INTO usage_logs VALUES
(NULL)

--drop NULL constraint
ALTER TABLE usage_logs
	ALTER COLUMN message CHAR(255) NULL;

--inserts successfully
INSERT INTO usage_logs VALUES
(NULL)


--add NOT NULL constraint
TRUNCATE TABLE usage_logs;
ALTER TABLE usage_logs
	ALTER COLUMN message CHAR(255) NOT NULL;


--UNIQUE constraint
--Set UNIQUE constraint during table creation
CREATE TABLE usage_logs(
	logid INT UNIQUE,
	message CHAR(250)
);

INSERT INTO usage_logs VALUES
(NULL, 'test')

--Remove UNIQUE constraint from the table 
ALTER TABLE usage_logs
	DROP CONSTRAINT UQ__usage_lo__7838F2645A08E2A3

--Add UNIQUE constraint to the table 
ALTER TABLE usage_logs
	ADD CONSTRAINT unique_constraint
	UNIQUE (logid);

DROP TABLE usage_logs
--CHECK constraint
CREATE TABLE usage_logs(
	logid INT NOT NULL UNIQUE CHECK (logid > 10),
	message CHAR(250)
)

--fails
INSERT INTO usage_logs VALUES
(1, 'test')
--inserts
INSERT INTO usage_logs VALUES
(11, 'test')

--remove check constraint
ALTER TABLE usage_logs
	DROP CONSTRAINT check_id;

-- add check constraint
TRUNCATE TABLE usage_logs;
ALTER TABLE usage_logs
	ADD CONSTRAINT check_id
	CHECK (logid > 10);


--DEFAULT constraint
CREATE TABLE usage_logs(
	logid INT NOT NULL UNIQUE,
	message CHAR(250),
	msgdate DATETIME NOT NULL DEFAULT GETDATE()
);

INSERT INTO usage_logs(logid, message) VALUES
(2, 'test');

SELECT * FROM usage_logs;

--add DEFAULT constraint
ALTER TABLE usage_logs
	ADD CONSTRAINT def_date
	DEFAULT (GETDATE()) FOR msgdate;

--remove DEFAULT constraint
ALTER TABLE usage_logs
	DROP CONSTRAINT def_date