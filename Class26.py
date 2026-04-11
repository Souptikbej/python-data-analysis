#Abstraction 

from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def sound(self):
    print("Yhea you use me Because i am main Branch")


class Dog (Animal):
  def sound(self):
    return super().sound()
  def hello(self):
    print("I am franchicy")


obj=Dog()
obj.sound()
obj.hello()