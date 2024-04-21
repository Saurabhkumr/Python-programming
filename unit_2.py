# string manipulation

# str="saurabhkumar"
# print(str[0:6])
# print(str[0:6:2])
# print(len(str))
# print(str[-1:-6:-1]) 
# print(str[-4:-1])  #len-4 to len-1

s1="hello world"
# s2=s1
# s1+=" guys"
# print(s1)
# print(s2)

# print(s1.upper())
# print(s1.lower())
# print(s1.title())
# print(s1.count("l",0,5))
# print(s1.isalnum())  # also consider spaces 
# print(s1.capitalize())
# print(s1.find("o"))
# print(s1.index("rld"))
# print(s1.replace("hello","byebye"))
# s2=("hello","world")
# print("-".join(s1))
# print("-".join(s2))
# s3=('india is a grat country')
# print(s3.partition('a'))
# print(s3.split('a'))


# List : collection of items , oreders sequence , mutable

# l=[2,3,1,34,2,23,12,2,44]
# print(l)
# print(len(l))
# print(l[0:])
# print(l[0::2])
# print(l[-4:-1])
# print(l*2)
# print(3 in l)
# for i in l:
#   print(i)
  
# list=[i for i in range(10) if i%2==0]   # list comprehension
# print(list)  

# l2=[9,6,4,5]
# l.extend(l2)
# l.append(l2)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# l3=l.copy()

# print(l3)

# str="hello"
# list=list(str)
# print(list) 
# l.insert(2,99)

# print(l.count(2))
# print(min(l))
# print(sum(l))
# print(l.pop(4))
# l.remove(2)
# print(l)


# l1=[2,3,4,5]
# l2=[1,23,34,35]
# print("l1+l2 : ",l1+l2 )
# print("l1*4 : ",l1*4 )


# tuples : collection of element , immutable , hetrogenous

# t=(12,34,2,3,45,1)
# # t1=(3,4,"dd",5,6)
# # print(t+t1)
# # l=list(t)
# # l.sort()
# # print(tuple(l))
# print(t.count(2))
# print(t.index(45))
# print(len(t))


# Dictionary : mapping data structure , having element  key value pairs, ordered sequence

# dict={
#   "name":"Saurabh",
#   "age":21,
#   "course":"Mca"
# }
# print(len(dict))
# dict["college"]="bciit"
# print(dict)
# print(dict["age"])
# dict["age"]=25
# print(dict)
# dict2={23:44,24:55}
# dict.update(dict2)
# print(dict)
# print("name" in dict)
# # for key in dict:
# #   print(key,":",dict[key])
  
# for key , value in dict.items():
#   print(key,":",value)
  
# print(dict.keys())
# print(dict.values())

# print(dict.get("name"))
# dict.clear()
# print(dict)
# del dict


# file handling

# f=open('myfile.txt','a+')
# f.write(input("Enter the data to be appended : "))
# f.seek(0)
# text=f.read()
# print(text)
# print(f.tell())
# f.close()

# with open('myfile.txt','r') as f:
#   print(f.read())

# f=open('myfile.txt','r')
# while(True):
#   line=f.readlines()
#   print(line)
#   if not line:
#     break
# f.close()

  
# f=open('myfile.txt','w')
# l=['i','am','cricketer']
# f.writelines(l)
# f.close


# pickling :

import pickle
# f=open('f1.dat','wb')
# l=['bccit','ipu','college']
# pickle.dump(l,f)
# f.close()
# f=open('f1.dat','rb')
# print(pickle.load(f))

def write():
  f=open('f.dat','wb')
  a=input("enter your name : ")
  b=input("enter your age : ")
  c = input("enter your course : ")
  l=[a,b,c]
  pickle.dump(l,f)
  f.close()
  
def read():
  f=open('f.dat','rb')
  print(pickle.load(f))  
  
write()
read()