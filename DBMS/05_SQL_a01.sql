USE employee_db;

CREATE TABLE Department(
	Deptno DECIMAL(2) NOT NULL,
	Deptname VARCHAR(50) UNIQUE,
	Location VARCHAR(50),
	CONSTRAINT department_pk
		PRIMARY KEY(Deptno)
)

CREATE TABLE Employee(
	Empno DECIMAL(3) PRIMARY KEY,
	ManagerID DECIMAL(3),
	FirstName VARCHAR(20),
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
);

