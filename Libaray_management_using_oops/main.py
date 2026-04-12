import json
import random
import string
from pathlib import Path
from datetime import datetime

class Library:
  def unique_id(Prefix ='B'):
    u_id=""
    for i in range(5):
      u_id+=random.choice(string.ascii_uppercase +string.digits)
    return Prefix + "-" + u_id


  def add_book(self):
    self.book_name=input("Enter Book Name :")
    self.author=input("Enter author :")
    self.copies=int(input("Enter how many copies :"))

    book_dict={
      "id":Library.unique_id(),
      "book_name":self.book_name,
      "book_author":self.author,
      "book_copies":self.copies,
      "book_avalible":self.copies,
      "book_adds_on":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    print(book_dict)





obj=Library()
print("="*50)
print("Library Management System")
print("="*50)
print("1. Add Book")
print("2. List Books")
print("3. Add Members")
print("4. List Members")
print("5. Borrow Book")
print("6. Return Book")
print("0. Exit The System")
print("-"*50)

choise=int(input("What you want to do :"))

if choise==1:
  obj.add_book()