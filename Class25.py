#Polymorephisum


class Animal:
  name="Lion"
  def speak(self):
    print("Hello i rear")


class Human(Animal):
  name="Souptik"
  def speak(self):
    print("Hello my name is souptik")


obj2=Human()
obj2.speak()