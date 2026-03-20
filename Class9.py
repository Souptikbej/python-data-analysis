# Funcation print 
'''
def Greet():
  print("Hello souptik")
Greet()
'''
#Funcation Return 
'''
def Greet():
  return "Hello Souptik"
print(Greet())
'''
#Keywords Arguments
'''
def addition(a,b):
  print(a+b)
addition(b=10,a=30)
'''
#Parameter
'''
def addition(a,b):
  print(a+b)
addition(10,10)
'''
#Welcome Message
'''
def welcome_message(name):
    # Write your code here
    print(f"Welcome, {name}!")
name=input("")
welcome_message(name)
'''
#Multiplication table Function
'''
def print_table(n):
    if isinstance(n, int):
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
print_table(5)
'''
#Count Digit Function
'''
def count_digits(n):
    if not isinstance(n,int):
        print(0)
    n=abs(n)
    if n==0:
        print(1)
    else:
        c=0
        while n>0:
            c+=1
            n=n//10
        print(c)
count_digits(12345)
'''
#Sum of First n Naturals
'''
def sum_of_naturals(n):
    s=0
    for i in range (1,n+1):
        s=s+i
    print(s)
sum_of_naturals(5)
'''
#Reverse Number Function
'''
def reverse_number(n):
    if isinstance(n, int):
        s=0
        while n>0:
            r=n%10
            s=s*10+r
            n=n//10
    print(s)
reverse_number(123456)
'''
#Armstrong Number Function
'''
def check_armstrong(n):
    if isinstance(n,int):
        p=len(str(n))
        copy=n
        s=0
        while n>0:
            r=n%10
            s=s+r**p
            n=n//10
        if copy==s:
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")
check_armstrong(153)
'''
#Longest Consecutive sequence
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # check if it's the start of a sequence
        if num - 1 not in num_set:
            current = num
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest
n = int(input())
nums = list(map(int, input().split()))
print(longest_consecutive(nums))
