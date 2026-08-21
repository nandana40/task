use database1;
create table Employees (EmployeeID INT PRIMARY KEY,EmployeeName varchar(100) NOT NULL,Department varchar(50),Salary decimal(10,2),check (Salary >= 0),JoiningDate DATE);
select name,year,selling_price,fuel from [dbo].['CAR DETAILS FROM CAR DEKHO$'];
select * from [dbo].['CAR DETAILS FROM CAR DEKHO$'] where fuel = 'Diesel';
select * from [dbo].['CAR DETAILS FROM CAR DEKHO$'] where selling_price=600000;
select * from [dbo].['CAR DETAILS FROM CAR DEKHO$'] where owner ='Second Owner';