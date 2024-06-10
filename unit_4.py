# lambda function : dunction without name

double = lambda x : x*2
# sum = lambda x,y : x+y


def func(f,value):
  return value+f(value)

print(func(double,8))
# print(sum(5,9)) 
# print(double(4))



# list comprehension

# l1 = [n**2 for n in range(1,11) if n%2==0]
# l2 = [n**2 if n%2==0 else n**3 for n in range(1,11)]
# print(l1)
# print(l2)




# map , filter and reduce

# l=[1,2,3,4,5,6]
# l1=list(map(lambda x : x**2 , l))
# l1=list(map(double, l))
# print(l1)

# def even(x):
#   return x%2==0
# l2 = list(filter(lambda x : x%2==0 , l))
# l2 = list(filter(even, l))
# print(l2)

# from functools import reduce
# l3=reduce(lambda x,y : x+y , l)
# print(l3)


