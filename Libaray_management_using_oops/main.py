import json
import random
import string
from pathlib import Path
from datetime import datetime

class Library:
  databse="Libaray_management_using_oops/Library.json"
  data={"Books":[],"Members":[]}

  #Load exixting data to JSON or create your JSON
  if Path(databse).exists():
    with open(databse,"r") as f:
      content=f.read().strip()
      if content:
        data=json.loads(content)
  else:
    with open(databse,"w") as f:
      json.dump(data,f,indent=4)

  def unique_id(Prefix ='B'):
    u_id=""
    for i in range(5):
      u_id+=random.choice(string.ascii_uppercase +string.digits)
    return Prefix + "-" + u_id
  
  @classmethod
  def save_data(cls):
    with open(cls.databse,'w') as f:
      json.dump(cls.data,f,indent=4,default=str)


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
    Library.data["Books"].append(book_dict)
    Library.save_data()


  def list_books(self):
    if not Library.data["Books"]:
      print("Sorry no books found")
      return
    for b in Library.data["Books"]:
      print(f"{b['id']:12} {b['book_name']:25} {b['book_author']:12} {b['book_copies']:12}")
  

  def add_member(self):
    self.name=input("Enter the name :")
    self.email=input("Enter the email id :")
    member_dict={
      "id":Library.unique_id("M"),
      "member_name":self.name,
      "member_email":self.email,
      "borowed":[],
      "member_adds_on":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    Library.data["Members"].append(member_dict)
    Library.save_data()
    print("Member Added Successfully......")

  def list_members(self):
      if not Library.data["Members"]:
        print("Sorry no Members found")
        return
      for m in Library.data["Members"]:
        print(f"{m['id']:12} {m['member_name']:25} {m['member_email']:12}")
        if not m['borowed']:
          print("No Borowed Book")
        else:
          print(f"{m['borowed']:12}")


  def borrowed_book(self):
    member_id=input("Enter Member id :").strip()
    members=[i for i in Library.data["Members"] if i['id']==member_id]
    if not members:
      print("No such Id exist")
    member=members[0]
    book_id=input("Enter Book id :").strip()
    books=[i for i in Library.data["Books"] if i['id']==book_id]
    if not books:
      print("No such Id exist")
    book=members[0]

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
if choise==2:
  obj.list_books()
if choise==3:
  obj.add_member()
if choise==4:
  obj.list_members()
if choise==5:
  obj.borrowed_book()
if choise==6:
  obj.return_book()