-- select 5 letters from left and right of string
SELECT LEFT('Hello World', 5), RIGHT('Hello World', 5);

--lower case and upper case
SELECT LOWER('Hello'), UPPER('Hello');

--trim all space from begining and end
SELECT TRIM('    Hello     ')

--trim spaces from left and right
SELECT LTRIM('    Hello     '), RTRIM('    Hello     ');

--duplicate a string 5 times
SELECT REPLICATE('hi', 5);

--get date and time
--current timestamp
SELECT CURRENT_TIMESTAMP AS Date;
--current datetime
SELECT GETDATE() AS Date;
--get the UTC time
SELECT GETUTCDATE() AS Date;
--get the precise time
SELECT SYSDATETIME() AS Date;

--extract day, month, year
SELECT DATENAME(day, '2022/07/12') Day,
	DATENAME(month, '2022/07/12') Month,
	DATENAME(year, '2022/07/12') Year;
	
--extracting part of date as integer
SELECT DATEPART(day, '2022/07/12');
SELECT DATEPART(month, '2022/07/12');
SELECT DATEPART(year, '2022/07/12');

SELECT DAY('2022/07/12') Day,
	MONTH('2022/07/12') Month,
	YEAR('2022/07/12') Year;

--find the difference between days months or weeks
SELECT DATEDIFF(DD, '2022/07/12' ,'2022/08/10');
SELECT DATEDIFF(MM, '2022/07/12' ,'2022/10/10');
SELECT DATEDIFF(WK, '2022/07/12' ,'2022/10/10');


--mathematical functions
--square root
SELECT SQRT(4) 'square root';

--absolute value
SELECT ABS(-9) abs;

--next highest value
SELECT CEILING(5.3) ceiling;

--next lowest value
SELECT FLOOR(6.5) floor;

--find the power
SELECT POWER(5, 2) fivesquare;

--logarithm
SELECT LOG10(100) log10b100;
SELECT LOG(100) log100;

--return sign 
SELECT SIGN(-4) sign;

--pseudo random number
SELECT RAND(), RAND(), RAND();
--pseudo random number with seed 10
SELECT RAND(10), RAND(10), RAND(10);


--convert function
--convert expression to int
SELECT CONVERT(int, 30.55);

--convert string expressiont to datetime
SELECT CONVERT(datetime, '2020-08-25');

--convert to varchar of length 100
SELECT CONVERT(varchar, '2020-08-25', 101);


--cast function (similar to CONVERT, but available in other DBMS too)
--convert expression to datetime
SELECT CAST('2020-08-25' AS DATETIME);

--convert float into varchar of length 50
SELECT CAST(20.35 AS VARCHAR(50));



--SQL JOINS
-- > INNER JOIN
-- > OUTER JOIN
--	 > LEFT OUTER JOIN
--	 > RIGHT OUTER JOIN
--	 > FULL OUTER JOIN
-- > CROSS JOIN
-- > SELF JOIN

CREATE DATABASE training;
USE training;

CREATE TABLE trainee(
	id INT PRIMARY KEY IDENTITY,
	admission_no VARCHAR(45) NOT NULL,
	first_name VARCHAR(45) NOT NULL,
	last_name VARCHAR(45) NOT NULL,
	age INT,
	city VARCHAR(25) NOT NULL
);

CREATE TABLE fee(
	admission_no VARCHAR(45) NOT NULL,
	sem_no INT NOT NULL,
	course VARCHAR(45) NOT NULL,
	amount INT
);

CREATE TABLE semester(
	sem_no INT NOT NULL,
	sem_name VARCHAR(10)
);

INSERT INTO trainee(admission_no, first_name, last_name, age, city) VALUES
	(3354, 'Spider', 'man', 13, 'Texas'),
	(2135, 'James', 'Bond', 15, 'Alaska'),
	(4321, 'Jack', 'Sparrow', 14, 'California'),
	(4213, 'John', 'McClane', 17, 'New York'),
	(5112, 'Oprimus', 'Prime', 16, 'Florida'),
	(6113, 'Captian', 'Krik', 15, 'Arizona'),
	(7555, 'Harry', 'Potter', 14, 'New York'),
	(8345, 'Rose', 'Dawson', 13, 'California');

INSERT INTO semester(sem_no, sem_name) VALUES
	(1, 'First sem'),
	(2, 'Second sem'),
	(3, 'Third sem'),
	(4, 'Fourth sem');
	
INSERT INTO fee(admission_no, sem_no, course, amount) VALUES
	(3354, 1, 'Java', 20000),
	(7555, 1, 'Android', 20000),
	(4321, 2, 'Python', 18000),
	(8345, 2, 'SQL', 15000),
	(9345, 2, 'Blockchain', 16000),
	(9321, 3, 'Ethical Hacking', 17000),
	(5112, 1, 'Machine Learning', 13000);

SELECT * FROM trainee;
SELECT * FROM semester;
SELECT * FROM fee;

--INNER JOIN (default join)
--returns all records that have matching values in both tables
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, fee.amount
	FROM trainee
	INNER JOIN fee ON trainee.admission_no = fee.admission_no;

--INNER JOIN with 3 tables
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, fee.amount, semester.sem_name
	FROM trainee
	INNER JOIN fee ON trainee.admission_no = fee.admission_no
	INNER JOIN semester ON semester.sem_no = fee.sem_no;

--LEFT OUTER JOIN
--return all records from left table even if there are no matches from right table 
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, FEE.amount
	FROM trainee
	LEFT OUTER JOIN fee ON trainee.admission_no = fee.admission_no;

--RIGHT OUTER JOIN
--return all records from right table even if there are no matches from left table 
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, FEE.amount
	FROM trainee
	RIGHT OUTER JOIN fee ON trainee.admission_no = fee.admission_no;

--FULL OUTER JOIN
--return all records from right as well as left table will be returned
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, FEE.amount
	FROM trainee
	FULL OUTER JOIN fee ON trainee.admission_no = fee.admission_no;

--SELF JOIN
--A table is joined to itself
SELECT T1.first_name, T1.last_name, T2.city
	FROM trainee T1, trainee T2
	WHERE T1.admission_no = T2.admission_no
	AND T1.city = T2.city
	ORDER BY T2.city;

SELECT T1.first_name, T1.last_name, T2.city
	FROM trainee T1, trainee T2
	WHERE T1.admission_no != T2.admission_no
	AND T1.city = T2.city
	ORDER BY T2.city;

--CROSS JOIN
SELECT * FROM trainee
	CROSS JOIN fee;

SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, fee.amount
	FROM trainee
	CROSS JOIN fee
	WHERE trainee.admission_no = fee.admission_no;

--Stored procedures
CREATE PROCEDURE traineeAgewiseList
AS
BEGIN
	SELECT first_name, age, city
	FROM trainee
	ORDER BY age;
END;

--execute SP
EXEC traineeAgewiseList;

--modify SP
ALTER PROCEDURE traineeAgewiseList
AS 
BEGIN
	SELECT admission_no, first_name, age, city
	FROM trainee
	ORDER BY age;
END;

--list all stored procedures in current db
SELECT * FROM sys.procedures;

--remove stored procedure 
DROP PROCEDURE traineeAgewiseList;

--pass parameters into stored procedures
CREATE PROCEDURE getTraineesFromCity (@city VARCHAR(20))
AS 
BEGIN
	SET NOCOUNT ON;	--hide rows modified message
	SELECT first_name, last_name, age, city
	FROM trainee
	WHERE city = @city
END;

EXEC getTraineesFromCity 'New York';

--return parameter form stored procedure
CREATE PROCEDURE getTraineeCount (@traineeCount INT OUTPUT)
AS
BEGIN
	SELECT @traineeCount = COUNT(id) FROM trainee;
END;

--recieving output from stored procedure
--step1 declare the variable to hold the output
DECLARE @TraineeCount INT
--step2 executing the stored procedure
EXEC getTraineeCount @TraineeCount OUTPUT;
--step3 print the TraineeCount
SELECT @traineeCount;


--Subquery
--Subquery in SELECT
SELECT * FROM trainee
	WHERE id IN (SELECT id FROM trainee WHERE age > 14);

--Subquery in DELETE 
DELETE FROM trainee 
	WHERE admission_no IN (SELECT admission_no FROM trainee WHERE admission_no = 3354);


--VIEWS
CREATE VIEW [ny trainees] AS
SELECT first_name, last_name, city
FROM trainee
WHERE city = 'New York';

SELECT * FROM [ny trainees];


--Triggers
--Creating a DDL trigger (for events of create, alter, drop)
CREATE TRIGGER dont_play_withmydb
ON DATABASE FOR create_table, alter_table, drop_table
AS
PRINT 'NOT ALLOWED !! IN MY DB'
ROLLBACK;

CREATE TABLE test(id INT);

--delete the trigger
DROP TRIGGER dont_play_withmydb ON DATABASE;


--Creating DML Trigger (for events of insert, update, delete)
--AFTER trigger
CREATE TRIGGER msg_after_insert
ON trainee
AFTER INSERT AS
BEGIN
	PRINT 'Inserted fine'
END;

--Testing the DML Trigger
INSERT INTO trainee(admission_no, first_name, last_name, age, city) VALUES
	(3354, 'Spider', 'man', 13, 'Texas');

--Deleting the After DML Trigger
DROP TRIGGER msg_after_insert;

--Create trainee_backup table
CREATE TABLE trainee_backup(
	id INT PRIMARY KEY IDENTITY,
	admission_no VARCHAR(45) NOT NULL,
	first_name VARCHAR(45) NOT NULL,
	last_name VARCHAR(45) NOT NULL,
	age INT,
	city VARCHAR(25) NOT NULL
);

--Create and After Trigger which can backup data to another table
CREATE TRIGGER backup_trainees
ON trainee
AFTER INSERT
AS
BEGIN
	SET NOCOUNT ON;
	
	DECLARE @admission_no INT
	DECLARE @age INT
	DECLARE @first_name VARCHAR(45)
	DECLARE @last_name VARCHAR(45)
	DECLARE @city VARCHAR(45)

	SELECT
		@admission_no	= I.admission_no,
		@first_name		= I.first_name,
		@last_name		= I.last_name,
		@age			= I.age,
		@city			= I.city
	FROM INSERTED I

	INSERT INTO trainee_backup
	VALUES(@admission_no, @first_name, @last_name, @age, @city);
	PRINT 'Values inserted into both trainee and backup tables'
END;

INSERT INTO trainee(admission_no, first_name, last_name, age, city) VALUES
	(3377, 'Super', 'man', 13, 'USA');

SELECT * FROM trainee_backup;

--INSTEAD OF Trigger
CREATE TRIGGER doinsteadofinsert
ON trainee
INSTEAD OF INSERT
AS
BEGIN
	PRINT 'values not inserted'
END;