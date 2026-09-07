use Database1 


CREATE TABLE Employees2 (
    Employee_id INT PRIMARY KEY,
    Employee_name VARCHAR(50),
    Department VARCHAR(30),
    City VARCHAR(30),
    Salary DECIMAL(10,2),
    Experience INT,
    Age INT
);


insert into Employees2
(Employee_id, Employee_name, Department, City, Salary, Experience, Age)
values
(1, 'Arun Kumar', 'IT', 'Kochi', 55000, 3, 25),
(2, 'Anjali Nair', 'HR', 'Calicut', 42000, 2, 24),
(3, 'Rahul Das', 'IT', 'Bangalore', 75000, 6, 30),
(4, 'Sneha Thomas', 'Finance', 'Kochi', 62000, 5, 28),
(5, 'Vishnu Raj', 'IT', 'Calicut', 68000, 4, 27),
(6, 'Fathima Ali', 'HR', 'Kochi', 48000, 3, 26),
(7, 'Nikhil Menon', 'Finance', 'Bangalore', 80000, 7, 32),
(8, 'Amal Dev', 'IT', 'Kochi', 59000, 4, 26),
(9, 'Meera Joseph', 'HR', 'Bangalore', 51000, 5, 29),
(10, 'Sanjay Kumar', 'Finance', 'Calicut', 57000, 3, 25),
(11, 'Anu Krishnan', 'IT', 'Bangalore', 72000, 5, 29),
(12, 'Ramesh Babu', 'HR', 'Kochi', 45000, 2, 23),
(13, 'Akhil Raj', 'Finance', 'Kochi', 67000, 4, 27),
(14, 'Neha Suresh', 'IT', 'Calicut', 63000, 3, 25),
(15, 'Manu Mohan', 'HR', 'Calicut', 46000, 2, 24);

--1
select count(*) as Total_employees from  Employees2

--2
select sum(Salary) as Total_salary from  Employees2

--3
select AVG(Salary) as average_salary from  Employees2

--4
select MAX(Salary) as Highest_salary from Employees2

--5
select MIN(Salary) as lowest_salary from Employees2

--TASK 2
--1
select * from Employees2 where Department IN ('IT', 'HR')
--2
select *from  Employees2 where City IN ('Kochi', 'Calicut')
--3
select * from Employees2 where Salary IN (55000, 62000, 75000)

--TASK 3
--1
select * from Employees2 where Employee_name LIKE 'A%'
--2
select *from Employees2 where Employee_name LIKE '%n'
--3
select * from Employees2 where Employee_name LIKE '%ar%'
--4
select * from Employees2 where City LIKE 'K%'
--5
select * from  Employees2 where Employee_name LIKE 'A____'
--6
select  * from Employees2 where Employee_name LIKE '_____'
--7
select * from Employees2 where City LIKE '_o%'
