upper = 0
lower = 0
str = input("enter a string:")
for i in str:
    if i.isupper():
        upper += 1
    else :
        lower += 1
print("uppercase letters are :",upper)  
print("lowercase letters are :",lower) 

li = [12,33,56,86]
lar = li[0]
low = li[0]
for i in li:
    if i > lar:
        lar = i
    else:
        if i < low:
            low = i
print("Largest number : ", lar)
print("smallest number : ",low)

string = "programming"
count = 0

# number of vowels
for ch in string:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)

# list in reverse order

n = int(input("Enter the number of elements: "))
numbers = []
reverse_list = []

for i in range(n):
    num = int(input("Enter the element: "))
    numbers.append(num)
for i in range(n - 1, -1, -1):
    reverse_list.append(numbers[i])
print(reverse_list)

# 10 to 1 in reverse order

for i in range(n, 0, -1):
    print(i)

# palindrome or not   

num = input("Enter a number: ")
if num == num[::-1]:
    print("number is Palindrome")
else:
    print("Not a palindrome")

# positive ,negative or zero

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# armstrong or not

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
# crct    
    
num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")    

numbers = [10, 15, 30, 25, 30, 35]
even = []
odd = []
even_sum = 0
odd_sum = 0

for i in numbers:
    if i % 2 == 0:
        even.append(i)
        even_sum += i
    else:
        odd.append(i)
        odd_sum += i

print(" list:", numbers)
print("Even numbers:", even)
print("Sum of even numbers:", even_sum)
print("Odd numbers:", odd)
print("Sum of odd numbers:", odd_sum)


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []
for i in list1:
    if i in list2:
        common.append(i)
print("Common elements:", common)


