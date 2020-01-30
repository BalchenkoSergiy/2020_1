-- Lesson 1
SELECT country
FROM HR.Employees;

SELECT DISTINCT country
FROM HR.Employees;

SELECT empid, lastname
FROM HR.Employees;

SELECT empid, lastname
FROM HR.Employees
ORDER BY empid;

SELECT empid, lastname
FROM HR.Employees
ORDER BY 1;

SELECT * FROM HR.Employees;

SELECT empid, firstname + ' ' + lastname AS fullname
FROM HR.Employees;

SELECT firstname, lastname, phone
FROM HR.Employees

--HomeWork
SELECT DISTINCT custid, YEAR(orderdate) AS 'Year'
FROM Sales.Orders
ORDER BY custid, YEAR(orderdate)