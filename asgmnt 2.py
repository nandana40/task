n = float(input("enter the purchase amount:"))
if n > 5000:
    discount = n * 20 / 100
    print("final payable amount:",n - discount)
elif n >= 2000 and n <= 5000:
    discount = n * 10 / 100
    print("final payable amount:",n - discount)
else:
    print("no discount")
print("final payable amount:",n)    
    

num = int(input("enter a number:"))
if num % 10 == 0:
    print("not valid")
elif num % 3 == 0:
    print("valid")
else:
    print("not valid")        



a = input("enter the first string:")
b = input("enter the second string:")
if len(a) == len(b) and sorted(a) == sorted(b):
    print("string is anagram")
else:
    print("string is not anagram")    
    
Username = "software"
password = "10072005"
user = input("enter the username:")
passwo = int(input("enter the password:"))
if user == Username and passwo ==  password:
    print("login succesfull:")
else:
    print("invalid:")          

num = int(input("enter a number:"))
if num % 5 == 0 and num % 3 ==0:
    print("fizz buzz")
elif num % 5 == 0:
    print("buzz")
elif num % 3 == 0:
    print("fizz")
else:
    print("invalid")            

num = int(input("enter a number:"))
if num % 2 == 0:
    if num % 4 == 0:
        print("number is divisible by 2 and 4:")
    else:
        print("the number is divisible by 2 but not by 4")
else:
    print("invalid") 
           
           
name = input("enter your name:")
age = int(input("enter your age:"))
percentage = float(input("enter the exam percentage:"))
income = int(input("enter your annual income:"))
scholar = input(" receiving  another scholarship?(Yes or No):")
if age >= 17 and age <= 25 and income < 800000 and scholar  == "No":
    if percentage > 85:
        print("eligible for full scholarship")
    elif percentage >= 70 and percentage < 85:
        print("eligible for partial scholarship:")
    else:
        print("Not eligible")
else:
    print("Not eligible")        

sslc = input("Have you passed tenth?(Yes or No:)")
if sslc == "Yes":
    plustwo = input("have you passed twelfth?(Yes or No:)")
    if plustwo == "Yes":
        percentage = float(input("enter your twelfth percentage:"))
        if percentage > 75:
            print("eligible for Engineering Admission")
        else:
            print("Eligible for General Degree")
    else:
        print("complete twelfth to proceed")
else:
    print("not eligible for admission")
            

age = int(input("enter your age:"))
income = float(input("enter your monthly income:"))
credit = int(input("enter your  credit score:"))
loan  = int(input("enter your loan amount:"))
if age < 21:
    print("loan denied: age must be 21")
elif income <25000:
    print("loan denied: income too low")
elif loan > income * 20:         
        print("Loan Denied: Loan amount too high compared to income")
else:
    if credit < 650:
        print("Loan Conditionally Approved with 15% interest")
    elif credit <= 750:
        print("Loan Approved with 10% interest")
    else:
        print("Loan Approved with 7% interest")
    
amount = int(input("enter an amount to withdraw:"))
if amount <= 0:
    print("invalid amount")
elif amount % 100 !=0:
    print("amount must be in  multiple of 100")
elif amount > 20000:
    print("maximum withdrawal limit is Rs.20000")
else:
    print("Transaction Succesfull")        
        