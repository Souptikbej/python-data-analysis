#Dunder/MAgic Methods

class Students:
  def __init__(self,name,roll):
    self.name=name
    self.roll=roll
  def __str__(self):
    return f"Your name is {self.name} and roll is {self.roll}."
  
obj=Students("Souptik",685)
print(obj)


class Shopping:
  def __init__(self,items):
    self.items=items
  
  def __len__(self):
    return len(self.items)

obj=Shopping(['appel','milk','bread'])
print(len(obj))


class Numbers:
  def __init__(self,numbers):
    self.numbers=numbers

  def __add__(self, custom):
    return self.numbers+custom.numbers
  
obj1=Numbers(12)
obj2=Numbers(12)
print(obj1+obj2)