# OOPS concept 

# class Person:
#   name="Saurabh"
#   age=21
#   def info(self):
#     print(f"My name is {self.name} and my age is {self.age}")

# class Person:
#   def __init__(self,name,age):
#     print("i am a person ")
#     self.name=name
#     self.age=age
#   def info(self):
#     print(f"My name is {self.name} and my age is {self.age}")

# a=Person()
# b=Person()
# b.name="Anmol"
# b.age=22
# b.info()
# a.info() 

# class Coder(Person):
#   def code(self):
#     print("i am coder")
    
    
# a= Person("saurabh",21)
# b=Coder("neha",24)
# b.info()
# a.info()


# class Car:
#   def __brake(self):
#     print("This is brake")
#   def _horn(self):
#     print("This is horn")

# a = Car()
# a._Car__brake()
# a._horn()

# class Sum:
#   name="Apple"
#   @staticmethod
#   def add(a,b):
#     return a+b
  
# a=Sum()
# print(a.name)
# print(a.add(5,5))

# #operator overloading

# class Vector:
#   def __init__(self,x,y,z):
#     self.x=x
#     self.y=y
#     self.z=z
#   def __add__(self,other):
#     return f"{self.x+other.x}i + {self.y+other.y}j + {self.z+other.z}k"  
  
# v1 = Vector(2,3,4)
# v2 = Vector(6,4,6)
# print(v1+v2)


# class Complex:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y
#   def __add__(self,other):
#     return f"{self.x+other.x}+{self.y+other.y}i"
  

# x1 = Complex(int(input("Enter the real part : ")),int(input("Enter the imaginary part : ")))    
# x2 = Complex(int(input("Enter the real part : ")),int(input("Enter the imaginary part : ")))    
# print(x1+x2)

# from abc import ABC , abstractmethod
# class Car(ABC):
#   @abstractmethod
#   def brake():
#     pass

# a=Car()


# class Square():

#   def sqr(self):
#     try:
#       a=int(input("enter the num : "))
#       print(a**2)
#     except:
#       print("enter valid input")

# a = Square()
# a.sqr()

# import math

# print(math.ceil(5.5))

# from math import *

# print(floor(5.5))

# import random

# l=[5,3,54,6,3,32,55]
# print(random.choice(l))
# print(random.randint(3,88))

import statistics

l=[6,4,3,5,3,3]
print(statistics.mean(l))
print(statistics.mode(l))