#Lambda
sqare= lambda a : a**2 
print(sqare(12))
add= lambda a,b : print(a+b)
add(10,20)

#Map 
#Purpose :- Apply funcation to every item of an iterabale and return a new items
#Syntax = map(function , iterable)
a=[1,2,3,4]
l=map(lambda x : x**2 , a)
print(list(l))

#Filter
#Purpose :- Filter items from an iterable bsed on a condition
#Syntax = filter (function,iterable)
a=[1,2,3,4,5,6]
l=[]
l= filter(lambda x : x%2==0 , a)
print(list(l))

#Zip
#Purpose :- Combine multipal iterable into pair of elements
#Syntax = zip(iterable1,iterable2,.....)
name=["Souptik","Ankit","Rupam"]
age=[23,22]
comb=zip(name,age)
print(dict(list(comb)))


#Comprehensions
a=[1,2,3,4,5,6,7,8,9,10,12,26,98,56,31]
li=[i for i in a if i%2==0]
print(li)#list

se={i for i in a if i%2==0}
print(se)#Set

dic={i:i**2 for i in a if i%2==0}
print(dic)#dictionary


#Generators
#Purpose :- Generators are a special type of iterator that generate items one by one instead of storing the entire sequence in memory
#Why use them : Savs memory for large datasets
#Effecient for lazy evalution (compute values only when needed)
def my_generator():
  for i in range(5):
    yield i
gen= my_generator()
print(next(gen))
print(next(gen))
print(list(gen))


#Decorators
def my_decorator(func):
  def wrapper():
    print("Hello i will print before")
    func()
    print("Hello i will print after")
  return wrapper

@my_decorator
def say_hello():
  print("hello")
say_hello()