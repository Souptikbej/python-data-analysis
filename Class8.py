#Question 1 : Print Each Digit (Reverse Order)
'''
n= int(input("Enter a number : "))
s=0
while n!=0:
  r=n%10
  s=s*10+r
  n=n//10
print(s)
'''
#Question 2 : Sum of Digit ( 123 -> 1+2+3=6)
'''
n= int(input("Enter a number : "))
s=0
while n!=0:
  r=n%10
  s+=r
  n=n//10
print(s)
'''
#Question 3 : Palindrome Number Check 
'''
n=int(input("Enter a number : "))
n1=n
s=0
while n!=0:
  r=n%10
  s=s*10+r
  n=n//10
if s==n1:
  print("Palindrome")
else:
  print("Not Palindrome")
'''
#Question 4 : Automorphic Number
n= int(input("Enter a number : "))
copy=n
square=n**2
c=0
while n!=0:
  c+=1
  n=n//10
x = square % (10**c)
if copy==x:
  print("Automorphic Number")
else:
  print("Not Automorphic Number")