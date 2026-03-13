'''
for i in range(1,41):
  print(i)
'''
'''
for i in range(-10,11,1):
  print(i)
'''
'''
for i in range(35,4,-1):
  print(i)
'''
'''
n=int(input("Enter number you want table of :- "))
for i in range(n,(n*10)+1,n):
  print(i)
'''

#Question 1 : print "Hello World" n Times
'''
n=int(input("Tell me how many times u wants to print : "))
for i in range (1,n+1):
  print(f"{i} Hello World")
'''
#Question 2 : print Numbers from 1 to n
'''
n=int(input("Tell me how many numbers u wants to print : "))
for i in range (1,n+1):
  print(i)
'''
#Question 3 : print Numbers from n to 1
'''
n=int(input("Tell me how many numbers u wants to print : "))
for i in range (n,0,-1):
  print(i)
'''
#Question 4 : Sum of Natural Numbers (1 to n)
'''
n=int(input("Tell me how many numbers u wants to Sum : "))
a=0
for i in range (1,n+1):
  a+=i
print(f"Sum of Natural Number : {a}")
'''
#Question 5 : Factorial of a Number
'''
n=int(input("Tell me which number Factorial you want : "))
a=1
for i in range (1,n+1):
  a*=i
print(f"Factorial of {n} is : {a}")
'''
#Question 6 : Sum of Even & Odd Numbers in range
'''
n=int(input("Tell me your range : "))
even=0
odd=0
for i in range(1,n+1):
  if i%2==0:
    even+=1
  else:
    odd+=1
print(f"Counts of Even number is {even}\nCounts of Odd number is {odd}")
'''
#Question 7 : print all Factors of a number
'''

n=int(input("Tell me what number factors you wnats : "))
for i in range(1,n+1):
  if n%i==0:
    print(i)
'''
#Question 8 : Sum of all Factors
'''
n=int(input("Tell me what number factors sum you wnats : "))
s=0
for i in range(1,n+1):
  if n%i==0:
    s+=i
print(f"Sum of all Factors of {n} is : {s}")
'''
#Question 9 : Power Calculation (a^b)
#Question 10 : Prime Number Check