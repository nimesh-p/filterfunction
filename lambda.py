
#without using lambda function
def sum(a,b):
    return a > b
print(sum(15,5))    

#using lambda functon
sum=lambda a,b: a+b
print(sum(5,5))


# using map function

a = [1,1,2, 3, 4]
b = [17,17, 12, 11, 10]
c = [-1,-1, -4, 5, 9] 

result=list(map(lambda x,y,z: x + y + z,a,b,c))
print(result)

#with set in map
result=set(map(lambda x,y,z: x + y + z,a,b,c))
print(result)

#othe example 
num=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda x: x%2==0,num))
print(result)



#filter function

num=[1,2,3,4,5,6,7,8,9,10,4,3,2,6,10]
result=list(filter(lambda x: x%2==0,num))
tot=list(filter(lambda n: n+2,num))
print(result)
print(tot)


#using set function
result=set(filter(lambda x: x%2==0,num))
print(result)

#reduce function
from functools import reduce
list = [1,2,3,4,5]
print(reduce(lambda  x,y: x+y,list))
print(reduce(lambda x, y: x*y, range(1,101)))