### 01:06:17 take screenshot and write the explanation if not provided in the notes.
#Learn what to do if .pyc corrupted, how to create new .venv


#Data Types and Conditional Statements
#from operator import truediv

#Data Types - Integer
num1=10
num2=20
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1*num2)
print()

#Data Types - String
name="Python"
new_name='Python' # "" or '' are same in Python.
print(name)
print(new_name)
print()

#Data Types - Float
a=10.5
b=30.2
print(a+b)
print()


# Debugging - type()
#integer
a=10
print(a)
print(type(a))
print()
# type is a pre-defined function to identify data types, only used for debugging purpose.
# When working with different libraries, used during comparing or typecasting.
#float
a=20.5
print(a)
print(type(a))
print()
#string
a="Rachit"
print(a)
print(type(a))
print()
#list
a=[]
print(a)
print(type(a))
print()
#tuple
a=()
print(a)
print(type(a))
print()
#dictionary
a={}
print(a)
print(type(a))
print()
#boolean
a=True
print(a)
print(type(a))
print()
#NoneType
a=None #reserved keyword, cannot be changed.
print(a)
print(type(a))
print()

#Conditional Statements - if
#indentation in python is important, same has to be followed to avoid compilation issues.
x=int(input("Enter your Marks: "))
if x>=40:
    print("Pass")
else:
    print("Fail")
print()
#earlier what we used; all values assigned manually is called hardcoding the data.

#type conversion or called type casting.
a=10
print(type(a))

#float is pre-defined function which converts any data to float - type casting
b=float(a)
print(b)

c="10"
print(c)
print(type(c))
d=int(c)
print(d)
print(type(d))
#above or below are same
c=int("10")
print(type(c))

#input() built in method. It takes default input as str.
#for below, it is a good idea to use float() if all the output is expected in float.
num1=input("Please enter first number") #although we enter a number, it takes as str by default.
num1=float(num1) #type conversion or typecasting from str to float. IMP in real life
print(type(num1))

num2=input("Please enter second number")
num2=float(num2)
print(type(num2))

num3=input("Please enter third number")
num3=int(num3)
print(type(num3))

print(num1+num2+num3)
#python is a interpretor language, it will execute statement by statement. The moment it finds error, it will terminate without going any further.
#enter a float value it above and debug


#--Python General--
#Comments
#using a # in the beginning of the statement or use ''' entire para between single quotes including multiple lines'''

#case sensitive
a=10
A=20
print(a)
print(A)
print()

# this is to identify data types. It prints the latest.
# below example prints 20 because that is the latest memory stored, python takes in sequence, if i add print(a) after a=10 then it takes 10 and then 20
a=10
# print(a)
a=20
print(a)
print(a)

#variable rules
# 1a=90 # variable starting with a number and special characters in any place are not allowed.
# a_1 or a-1 is OK
# print(1a)
a1=90
print(a1)
print()
#%b=100
#print(%b)

#Arathmatic operators
a=10+5
print(a)
#or below are same
print(10+5)
print()
#addition
a=int(10)
print(type(a))
b=int(5)
print(a+b)
print()
#substraction
a=int(10)
b=int(5)
print(a-b)
print()
#multiplication
a=int(10)
b=int(5)
print(a*b)
print()
#division
#In Python, the division operator / always performs floating-point division.
#So even if both operands are integers, the result will be a float.
#If you want integer division, you should use the // operator.
a=int(10)
b=int(5)
print(type(a/b))
print()
#modulas
a=int(11)
b=int(2)
print(a%b) #modulas prints remainder
print()
#logical operator such as ">, <, >=, and, or" used in comparison. And and or are reserved keywords.
#when we use "and" and "or" in one statement, it evaluates from left to right.
print(50>10 or 50>30) #output True

#string concept - escape character (there are multiple escape characters.
name="Python is \"programming\" language" #scape characters tell python to escape "" in the statement.
print(name)

#capturing big or lengthy messages, use """ """ or ''' '''
msg=("""Selenium is for Web Automation
     asdasd
     asdasd
     asdasd
     asdasd
     """)
print(msg)
# we can use """ or ''' inside variable and outside variable, it works as comments.


#python supports 3 types of casing | most recommended in python is snack-case = age_to_calculate.
# camelcase - numberToStore
# snack-case - age_to_calculate
# generic-case - lengthy variable name like NumberToStore

#Python Package vs Python Directory in Pycharm - read cloud notes live

'''
Following concepts are Important to know - refer cloud notes live
prime numbers
even odd numbers
natural numbers
complex numbers
armstrong numbers
palindrome numbers
'''