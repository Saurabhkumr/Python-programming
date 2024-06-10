f = open('myfile.txt','r')
f1 = open('file2.txt','w')

# x=f.read()
# print(x)

# str = input("enter the data : ")
# f.write(str)
# v=0
# c=0
# l=0
# while(True):
#   line = f.readline()
#   if not line:
#     break
#   l=l+1
#   for i in line:
#     if i in 'aeiou':
#       v=v+1
#     elif i.isalpha():
#       c=c+1
#   if(l%2!=0):
#     f1.write(line)

line=f.readlines()
print(line)
      
  
# print("vowel : ",v)
# print("consonants : ",c)
# print("lines : ",l)




f.close()
f1.close()