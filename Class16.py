#try and except
'''
try:
  a=int(input("Enter an integer : "))
  b=int(input("Enter an integer : "))
  c=a/b
  print("c = ",c)
except ZeroDivisionError as zde:
  print("Dinominator is 0")
  print(zde.args)
  print(zde)

except ValueError: 
  print("Unable to convert string to int")

except:
  print("Some unknown error")
'''
#try and except and else
try:
  lst=[10,20,30,40,50]
  for num in lst:
    i=int(num)
    j=i*i
    print(i,j)
except NameError:
  print(NameError.args)
else:
  print("Total numbers processed",len(lst))
  del(lst)

#WAP to recived infinity positive integer as input and print its square, If a nagative number is entered then raise an exception,display a relevant error message and make a graceful exit.
try:
  while True:
    a=int(input("Enter a positive number : "))
    if a>=0:
      print(a*a)
    else:
      raise ValueError("Nagetive number")
except ValueError as ve:
  print(ve)