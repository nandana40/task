#whi.e

#..
str = input("enter a string:")
i = 0
while i < len(str):
    if str[i] != " ":
        print(str[i])
        i += 1

#..        
names = ["ankit","abhay","sangeeth","john","aleena"]
i = 0
while i < len(names) :
    if len(names[i])> 4:
        print(names[i])
        i += 1  
  
 #..       
str = input("enter a string:")
i = 0 
count = 0
while i < len(str):
    if str[i].isupper():
        count += 1
        i += 1
print("uppercase letters :",count)

#..
words = ["apple","banana","cherry"]
i = 0
while i < len(words):
    print(words[i],"=",len(words[i]))
    i += 1
    
#..    
str = input("enter a string:")
i = 0
count = 0
while i < len(str):
    if str[i] in "a,e,i,o,u":
      count += 1
    i += 1
print(count) 



# functions         
def dup(l):
    a = []
    for i in l:
        if i not in a:
            a.append(l)

    return a
b = [20,45,21,98,20,45]
print(dup(b))    

def count(sent):
    words = sent.split()
    return len(words)
str = input("enter a sentence:")
print("count of words :",count(str))

def palindrome(str):
    if str == str[::-1]:
        return("palindrome")
    else:
        return("not palindrome")
str = input("enter a string")
print(palindrome(str))    

def sum(l):
    sum = 0
    for i in l:
        sum += 1
    return sum
numbers = [8,2,3]
print(sum(numbers))
    
def average(a,b,c):
    average = (a + b + c)/3
    return average
a = int(input("enter first no:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
print(average(a,b,c))

def even(l):
    result =[]
    for i in l:
        if i % 2 == 0:
            result.append(i)

    return result       
numbers = [6,8,4,3,6,9,10]
print(even(numbers))


def count(number):
    count = 0
    for i in str(number):
        count += 1
    return count
number = int(input("enter a number:"))
print(count(number))
    
    
def  sum(even):
    sum = 0
    while even > 0:
        digit = even %  10
        if digit % 2 == 0:
            sum += digit
        even = even // 10
    return sum
even = 56789
print(sum(even))            
