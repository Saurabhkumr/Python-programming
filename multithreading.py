# from threading import *
# from time import *

# class Hello(Thread):
#   def run(self):
#     for i in range(5):
#       print("Hello")
#       sleep(1)
      
      
      
# class Bye(Thread):
#   def run(self):
#     for i in range(5):
#       print("Bye")
#       sleep(1)
      
# t1=Hello()
# t2=Bye()

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print("My name is saurabh")


# synchronization of thread - using lock

import threading
import time
# lock = threading.Lock()
# x=10

# def double():
#   global x,lock
#   lock.acquire()
#   while x<100:
#     x=x*2
#     print(x)
#     time.sleep(1)
#   lock.release()
  
  
  
# def half():
#   global x,lock
#   lock.acquire()
#   while x>1:
#     x=x//2
#     print(x)
#     time.sleep(1)
#   lock.release()
  
  
# t1 = threading.Thread(target=double)
# t2 = threading.Thread(target=half)
# t1.start()
# t2.start()


# using semaphore

s=threading.Semaphore(3)

def display(thread_num):
  print(f"{thread_num} tring to acquiring")
  s.acquire()
  print(f"{thread_num} granted ")
  time.sleep(5)
  print(f"{thread_num} releasing ") 
  s.release()
  
for i in range(11):
  t1 = threading.Thread(target=display,args=(i,))
  t1.start()
  time.sleep(1)