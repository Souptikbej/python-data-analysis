from pathlib import Path
import os

def c_folder():
  try:
    name=input("Enter tell your folder name:- ")
    p=Path(name)
    p.mkdir()
    print("Folder Created Successfully...")
  except Exception as err:
    print("Sorry Error occured as :",err)

def r_file_folder():
  p=Path("")
  items=list(p.rglob('*'))
  for i,v in enumerate(items):
    print(f"{i+1} : {v}")

def u_folder():
  try:
    r_file_folder()
    old_name=input("Please tell which folder you want to update :- ")
    p=Path(old_name)
    if p.exists() and p.is_dir():
      new_name=input("Please teel your new folder name :- ")
      new_p=Path(new_name)
      p.rename(new_p)
      print("Your folder name is update successfully..")
    else:
      print("Sorry no such folder exits..")
  except Exception as err:
    print("An error occured as {err}")

def delete_folder():
  try:
    r_file_folder()
    name=input("Please tell which folder you want to delete : ")
    p=Path(name)
    if p.exists()  and  p.is_dir():
      p.rmdir()
      print("Folder Deleted Successfully..")
    else:
      print("No such folder exist")
  except Exception as err:
    print("An error occured as {err}")


print("Choose any one of them :")
print("1. Create a folder")
print("2. Read files and folders")
print("3. Update the folder")
print("4. Delete the folder")

choose=int(input("Please choose your option : "))

if choose==1:
  c_folder()
if choose==2:
  r_file_folder()
if choose==3:
  u_folder()