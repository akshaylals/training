USE employee_db

--create table
CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
	cust_name VARCHAR(50),
	city VARCHAR(50),
	grade INT,
	sales_amount INT
);

--insert data
INSERT INTO customers
VALUES(3002, 'Anna Anthony', 'New York', 100, 5001),
(3007, 'Samantha Carl', 'New York', 200, 4001),
(3005, 'Jacob James', 'California', 200, 2002),
(3008, 'Sophie Green', 'London', 300, 6002),
(3004, 'Joe William', 'Paris', 300, 9000);

--total number of customers
SELECT COUNT(*) FROM customers;

--Highest graded customers
SELECT * FROM customers
WHERE grade = (SELECT MAX(grade) FROM customers);

--Lowest graded customers
SELECT * FROM customers
WHERE grade = (SELECT MIN(grade) FROM customers);

--Average sales amount
SELECT AVG(sales_amount) AS 'Average sales amount'
FROM customers;

--Total sales amount
SELECT SUM(sales_amount) AS 'Total sales amount'
FROM customers;