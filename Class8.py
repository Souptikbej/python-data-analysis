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
  print("Palindrome Number")
else:
  print("Not Palindrome Number")
'''
#Question 4 : Automorphic Number
'''
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
'''
#Question 5 : Check wheather a given number is a Harshad number or not
'''
n=int(input("Enter number : "))
store=n
n=abs(n)
s=0
if(n<=0):
  print("Not Harshad Number")
else:
  while(n!=0):
    r=n%10
    s+=r
    n=n//10
  if (store%s==0):
    print("Harshad Number")
  else:
    print("Not Harshad Number")
'''
#Question 6 :  
'''
sum = 0
count = 0
while True:
    n = int(input())
    if n < 0:
        break
    sum += n
    count += 1
if count == 0:
    print(0)
else:
    print(sum / count)
'''
#Question 7 : Strong Number Check eg, 145=1!+4!+5!
'''
n=int(input(""))
copy=n
s=0
while(n!=0):
  r=n%10
  f=1
  for i in range(1,r+1):
    f=f*i
  s+=f
  n=n//10
if copy==s:
  print("Strong Number")
else:
  print("Not Strong Number")
'''