# Write your MySQL query statement below
SELECT Name as Customers
FROM Customers
LEFT OUTER JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE Orders.Id IS NULL;
