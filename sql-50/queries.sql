

--comments in sql


-- create a table
CREATE TABLE PERSONS(
     PERSONID int,
     FIRSTNAME varchar(255),
     LASTNAME varchar(255),
     EMAIL varchar(255)
)


-- add a record to the db 
INSERT INTO PERSONS(PERSONID, FIRSTNAME, LASTNAME, EMAIL) VALUES (4,'EDWARD','JONAS','EDWARD.JONAS@EXAMPLE.COM')

-- remove a record from a db
DELETE FROM PERSONS WHERE PERSONID = 4

-- add a column to a table
ALTER TABLE PERSONS ADD "AGE" int;

-- remove a column from a table
ALTER TABLE PERSONS DROP COLUMN "AGE"



-- select all
SELECT * FROM Persons

-- select all where 
SELECT * FROM PERSONS WHERE FIRSTNAME = 'John'

-- order data elements, highest to lowest
SELECT FIRSTNAME, LASTNAME FROM PERSONS ORDER BY FIRSTNAME DESC

-- select all names starting with j
SELECT FIRSTNAME FROM PERSONS WHERE FIRSTNAME LIKE "j%"

-- select all names starting between a-c
SELECT FIRSTNAME FROM PERSONS WHERE FIRSTNAME LIKE "[abc]%"

-- select all email addresses from gmail
SELECT EMAIL FROM PERSONS WHERE EMAIL LIKE "%@gmail.com"

-- select all records where a person is between 40 to 50 years old
SELECT * FROM PERSONS WHERE AGE BETWEEN 40 AND 50


-- primary keys: column of distinct values used to uniquely represent a single record
-- foreign keys: column of values related to column in a parent table, linking tables together

-- inner join: link all records occurring in one table with all records also occurring in another table
-- outer join: link all records occurring in both tables regardless of if they occur in each other
-- left join: link all records occurring in the left table with records of the left table that the right table has
-- right join: link all records occurring in the right table with records of the right table that the left table has

-- join syntax:
SELECT * 
FROM PERSONS 
INNER JOIN ORDERS 
ON PERSONS.PERSONID = ORDERS.PERSONID

