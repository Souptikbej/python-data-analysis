#Question 1 :Accept two numbers and print the greatest between them.
'''
a=int(input("Enter your fisrt number : "))
b=int(input("Enter your second number : "))
if a>b:
  print(f"{a} is greater than.")
elif b>a:
  print(f"{b} is greater than.")
else:
  print(f"{a} is equal to {b}")
'''


#Question 2 : Accept the gender from the user as char and print the respective greeting message
'''
gen = input("Please tell me your Gender (m/f): ")
if gen =='m':
  print("Hello Sir how are you .")
else:
  print("Hello Mam how are you .")
'''


#Question 3 : Accept an integer and check whether it is an even number or odd.
'''
num = int( input("Enter a number : "))
if num%2==0:
  print("Yes , it is a Even Number.")
else:
  print("No , it is a Odd Number.")
'''


#Question 4 : Accept name and age from the user. Check if the user is a valid voter or not. Ex- “hello shery you are a valid voter”
'''
name= input("Enter your name : ")
age = int(input("Enter your age : "))
if age>=18:
  print(f"hello {name} you are a valid voter")
else:
  print(f"hello {name} you are not eligible to vote")
'''


#Question 5 : Accept a year and check if it a leap year or not
'''
year= int(input("Enter year : "))
if (year%4==0 and year%100!=0) or year%400==0:
  print(f"Yes , {year} is a leap year.")
else:
  print(f"No ,{year} is not a leap year.")
'''

#Question 6 :Ask for purchase amount. Apply discounts based on Threshold:eg,above 1000->10%off , above 5000->20%off. Print final bill.
bill=int(input("Enter your bill amount : "))
if bill>=1000 and bill <=4999:
  print(f"You got 10% off on your Shopping\nYour final amount is : {(bill*90)/100}")
elif bill>=5000:
  print(f"You got 20% off on your Shopping\nYour final amount is : {(bill*80)/100}")
else:
  print("Sorry no discount avalible on your shopping.")