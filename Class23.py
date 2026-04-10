'''
#Inheritance
class Animal:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def show(self):
    print(f"Your name is : {self.name} and age is {self.age}")

class Human(Animal):#Single Level
  def __init__(self, name, age,number,group):
    super().__init__(name, age)
    self.number=number
    self.group=group

class Robots(Human):#Multilevel
  def __init__(self, name, age, number, group,date):
    super().__init__(name, age, number, group)
    self.date=date

obj=Animal("Lion",12)
obj2=Human("Souptik",23,7278663190,"o+")
obj3=Robots("Evon",2,203,"EV","10-10-2024")

'''
#Multiple 

class Animal:
  pass
class Human:
  pass
class Robots(Animal,Human):
  pass