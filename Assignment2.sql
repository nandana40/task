use Database1 


CREATE TABLE Employees1 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(30),
    city VARCHAR(30),
    salary DECIMAL(10,2),
    experience INT,
    age INT
);


insert into Employees1 
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
select count(*) as Total_employees from  Employees1

--2
select sum(Salary) as Total_salary from  Employees1

--3
select AVG(Salary) as average_salary from  Employees1

--4
select MAX(Salary) as Highest_salary from Employees1

--5
select MIN(Salary) as lowest_salary from Employees1

--TASK 2
--1
select * from Employees1 where Department IN ('IT', 'HR')
--2
select *from  Employees1 where City IN ('Kochi', 'Calicut')
--3
select * from Employees1 where Salary IN (55000, 62000, 75000)

--TASK 3
--1
select * from Employees1 where Employee_name LIKE 'A%'
--2
select *from Employees1 where Employee_name LIKE '%n'
--3
select * from Employees1 where Employee_name LIKE '%ar%'
--4
select * from Employees1 where city LIKE 'K%'
--5
select * from  Employees1 where Employee_name LIKE 'A____'
--6
select  * from Employees1 where employee_name LIKE '_____'
--7
select * from Employees1 where city LIKE '_o%'
