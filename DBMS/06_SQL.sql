USE training;

--Transactions
--Start a new transaction
BEGIN TRANSACTION
--SQL Statements
INSERT INTO semester (sem_no, sem_name) VALUES (5, 'sem 5');
UPDATE semester SET sem_name = 's5' WHERE sem_no = 5;
--commit transaction
COMMIT TRANSACTION


--Manual ROLLBACK
--Start a new transaction
BEGIN TRANSACTION
--SQL Statements
INSERT INTO semester (sem_no, sem_name) VALUES (6, 'sem 6');
UPDATE semester SET sem_name = 's6' WHERE sem_no = 6;
--rollback transaction
ROLLBACK TRANSACTION


--ROLLBACK transaction in case of error
--Start a new transaction
BEGIN TRANSACTION
--SQL Statements
INSERT INTO semester (sem_no, sem_name) VALUES (6, 'sem 6');
UPDATE semester SET sem_no = 's6' WHERE sem_no = 6;
--check for errors usign the system variable @@ERROR
IF(@@ERROR > 0)
BEGIN
	ROLLBACK TRANSACTION
END
ELSE
BEGIN
	COMMIT TRANSACTION
END


--ROLLBACK transaction in case of error automatically
--Start a new transaction
BEGIN TRANSACTION
--SQL Statements
INSERT INTO semester (sem_no, sem_name) VALUES (6, 'sem 6');
UPDATE semester SET sem_no = 's6' WHERE sem_no = 6;
--try to commit transaction, if fails will automatically rollback
COMMIT TRANSACTION


