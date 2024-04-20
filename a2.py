str="BCIIT IPU COLLEGE"
str=str.split(' ')
b=[]
for i in str:
  a=""
  for j in reversed(i):
    a+=j 
  b.append(a)
print(" ".join(b))  