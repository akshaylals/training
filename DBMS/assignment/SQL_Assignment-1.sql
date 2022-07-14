CREATE TABLE sales(
	orderID INT IDENTITY PRIMARY KEY,
	ordDate DATE DEFAULT GETDATE(),
	ordPrice MONEY,
	ordQty INT DEFAULT 1,
	custName VARCHAR(50) NOT NULL
);

INSERT INTO sales(ordDate, ordPrice, ordQty, custName) VALUES
('2020/11/22', 150, 2, 'John'),
('2020/07/10', 180, 2, 'Tom'),
('2020/06/13', 400, 5, 'Jerry'),
('2020/06/15', 320, 2, 'John'),
('2020/11/22', 800, 4, 'Bond'),
('2020/09/02', 730, 4, 'Chaplin'),
('2020/10/03', 1000, 2, 'Mickey');


--1. Count orders made by John
SELECT COUNT(orderID) 'Number of Orders' FROM sales WHERE custName = 'John';

--2. Number of unique customers
SELECT COUNT(DISTINCT custName) 'Unique customers' FROM sales;

--3. Total no. of items ordered by all.
SELECT SUM(ordQty) 'Total number of items' FROM sales;

--4. Avg number of items per order 
SELECT AVG(ordQty) 'Average no. of items per order' FROM sales;

--5. Avg Order Quantity with order Price > 300
SELECT AVG(ordQty) 'Average order qty with price > 300'
	FROM sales
	WHERE ordPrice > 300;

--6. Minimum price paid for any of the orders
SELECT MIN(ordPrice) 'Minimum price paid for any of the orders'
	FROM sales;

--7. All customers whose name ends with 'n'
SELECT custName FROM sales
	WHERE custName LIKE '%n';

--8. All unique customer's name from the table
SELECT DISTINCT custName 'Unique customers names' FROM sales;

--9. Total amount spent by each customers
SELECT custName, SUM(ordPrice) 'Total amount spent' FROM sales
	GROUP BY custName;

--10. Unique customers who have spent more than 700
SELECT DISTINCT custName 'Unique customers who spent more than 700'
	FROM sales
	WHERE ordPrice > 700;

--11. Customers who have ordered more than 3 items
SELECT custName 'customers who have ordered more than 3 times'
	FROM sales
	GROUP BY custName
	HAVING COUNT(custName) > 3;

--12. All who spent more than 600
SELECT custName 'All who spent more than 600'
	FROM sales
	WHERE ordPrice > 600;

--13. List orders in ascending order of price
SELECT * FROM sales ORDER BY ordPrice;

--14. List orders in descending order of price
SELECT * FROM sales ORDER BY ordPrice DESC;