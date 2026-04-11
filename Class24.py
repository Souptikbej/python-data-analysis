#Encasulation
class Animal:
  __name="lino"
  def hello(self):
    print(f"Hello my name is {super.nam}")

obj=Animal
print(obj.__name)