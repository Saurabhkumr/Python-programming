for i in range(1,10):
  if(i<5):
    i=i
  else:
    i=10-i
  for j in range(1,i+1):
    print(" * ",end='')
  for k in range(1,10-2*i+1):
    print("   ",end='')
  for j in range(1,i+1):
    print(" * ",end='')  
  print();  