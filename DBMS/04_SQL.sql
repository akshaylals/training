--ASCII: get ASCII value for A
SELECT ASCII('A');

--CHARINDEX: search substring inside a string
SELECT CHARINDEX('World', 'Hello World');

--CONCAT: join together two srtings
SELECT CONCAT('Hello', 'World');

--check how string sounds
SELECT 
	SOUNDEX('Test') Test,
	SOUNDEX('Testing') Testing;

SELECT
	SOUNDEX('Sent') Sent,
	SOUNDEX('Send') Send;

	
SELECT DIFFERENCE('Tom', 'Tomy') 'Tom Tomy';
SELECT DIFFERENCE('Tom', 'Tom') 'Tom Tom';
SELECT DIFFERENCE('Tom', 'foo') 'Tom foo';