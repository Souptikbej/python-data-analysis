#Question 1 :Accept two numbers and print the greatest between them.
a=int(input("Enter your fisrt number : "))
b=int(input("Enter your second number : "))

if a>b:
  print(f"{a} is greater than.")
elif b>a:
  print(f"{b} is greater than.")
else:
  print(f"{a} is equal to {b}")



#Question 2 : Accept the gender from the user as char and print the respective greeting message
gen = input("Please tell me your Gender (m/f): ")
if gen =='m':
  print("Hello Sir how are you .")
else:
  print("Hello Mam how are you .")


#Question 3 : Accept an integer and check whether it is an even number or odd.
num = int( input("Enter a number : "))

if num%2==0:
  print("Yes , it is a Even Number.")
else:
  print("No , it is a Odd Number.")


#Question 4 : Accept name and age from the user. Check if the user is a valid voter or not. Ex- “hello shery you are a valid voter”
name= input("Enter your name : ")
age = int(input("Enter your age : "))

if age>=18:
  print(f"hello {name} you are a valid voter")
else:
  print(f"hello {name} you are not eligible to vote")



#Question 5 : Accept a year and check if it a leap year or not
year= int(input("Enter year : "))
if (year%4==0 and year%100!=0) or year%400==0:
  print(f"Yes , {year} is a leap year.")
else:
  print(f"No ,{year} is not a leap year.")