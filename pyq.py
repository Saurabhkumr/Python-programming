# class Square:
  
#   def __init__(self,num):
#     self.num=num
#   def sq(self):
#     try:
#       result=self.num**2
#       print(result)
#     except Exception as e:
#       print(e)

# n1 = Square(input("enter number : "))
# n1.sq()



# class Complex:
#   def __init__(self,x,y,z):
#     self.x = x 
#     self.y = y
#     self.z = z
    
#   def __add__(self,value):
#     return f"{self.x+value.x}i + {self.y+value.y}j + {self.z+value.z}k "
  

# c1=Complex(3,4,5)
# c2=Complex(2,3,6)

# print(c1+c2)


class BankAccount:
  def __init__(self,name,acctno,balance):
    self.name=name
    self.acctno=acctno
    self.balance=balance

  def display(self):
    print(f"name is {self.name}")
    print(f"Acc_no is {self.acctno}")
    print(f"balance is {self.balance}")
   
  def deposit(self,x):
    self.balance=self.balance+x
    print(f"money deposited {self.balance}")
    
  def withdraw(self,x):
    self.balance=self.balance-x
    print(f"money withdraw {self.balance}")



c1 = BankAccount("saurabh",101,60000)
c1.display()
c1.deposit(40000)
c1.display()
c1.withdraw(50000)
c1.display()