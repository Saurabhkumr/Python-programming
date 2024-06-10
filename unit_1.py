# comment
 
'''
this
is multi 
line
comment
'''
# print("hello")

# tokens : single individual unit of meaningfull info.
# 1-identifiers
# 2-keywords
# 3-operators
# 4-literals
# 5-delimiter

# variable is name given to memory location
# identifier is name given to enity like class , func , variables 
# all variable are identifier but vise versa is not true

# data types:
# int 
# float
# string
# boolean
# list 
# tuples
# set
# dictionary

# types of operators:
# arithmetic : +,-,/,*,//(floor division , return quotient part)
# camparison
# assignement
# logical : AND(&) , or(|)
# identity operator (is)
# membership operator (in) (not in)

# a= True
# b= False
# print(a | b)
# print(a & b)
# print(a or b)
# print(a and b)

# print(5//2)

# a=[2,4]
# b={2,4}
# print(a is b) # is both a and b pointing to same object
# print(4 in a) # check 4 is in a 
# print(4 not in a) 

# operator precedence

# type casting
# a = (int)(4.5)
# print(a)
# a=[('a',2),('b',4)]
# print(dict(a))

# name = input("enter your name : ")
# print("My name is : "+name,end=' ')
# print("My name is : ",name)
# import sys
# sys.stdout.write("Hello, world!")
# print("hello , world")

# a="4"
# print(int(a))

# short circuit : By short-circuiting, we mean the stoppage of execution of boolean operation if the truth value of expression has been determined already.

# lazy evaluation : Lazy Evaluation is an evaluation strategy which delays the evaluation of an expression until its value is needed

# flow control

#if-else-elif

# a=4
# if(a>4):
#   print("hello")
# elif(a<4):
#   print("hii")
# else:
#   print("bye")    
  
  
# num = eval(input("enter a num : "))  # automatically ditect input type
# print(type(num))
# num = int(input("enter a num : ")) 
# print(type(num))


# for i in range(2,10,2):
#   print(i)
  
# i=1
# while(i<10):
#   print(i)
#   i+=1

# funtion

# def greethello():
#   print("hello")

# def greethello(name,ending):
#   print("hello"+ name + ending)

# greethello(name="saurabh",ending="kumar")  

# def greethello(name,ending="kumar"):
#   print("hello"+ name + ending)

# greethello(name="saurabh")  

# x=3
# def modify():
#   global x
#   x=5  #we can change  global variable using global keyword
#   y=8  #local variable
#   print(y)
#   print(x)
  
# print(x)
# modify()
# print(x)

# def fun(fruit):
#   for i in fruit:
#     print(i)

# food=["mango","banana","apple"]
# fun(food)    

# decorators

# def outer():
#   print("i am outer func")
#   def inner():
#     print("i am inner func")
#   inner()  
# outer()

# def greet(func):
#   def sum(a,b):
#     print("welcome...")
#     print(func(a,b))
#     print("thankyou..")
#   return sum

# @greet  # decorator
# def add(a,b):
#   return a+b

# add(4,8)


#reccursion

# def factorial(num):
#   if(num==1):
#     return 1
#   return num*factorial(num-1)

# print(factorial(4))


# iterator 



