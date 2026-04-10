#Attribute and Method

class Animal:
  name='Lion'       #Class Attribute

  def __init__(self,name,age):
    self.name=name  #Instance attribute
    self.age=age    #Instance attribute


  def speak(self):
    print("This is a Instance Method")
  
  @classmethod
  def clmethod(cls):
    print(f"Animal name is : {cls.name}\nThis is a Class Method")

  @staticmethod
  def hello():
    print("This is a Static Method")

obj=Animal("Tiger",10)#Instance attribute
print(obj.name)#Class Attribute

obj.speak()#instance method

obj.clmethod()#class method

obj.hello()#static method


#Student Registation System (Take name,age, number, blood group)

class Registration:
  def __init__(self,name,age,number,bloodg):
    self.name=name
    self.age=age
    self.number=number
    self.bloodg=bloodg
  def info(self):
    print(f"Hello your name is {self.name}\nYour age is {self.age}\nYour contact number is {self.number}\nYour Blood Group is {self.bloodg}")

student1=Registration("Souptik",23,7278663190,'A+')
student2=Registration("Surjo",23,7278563230,'B+')
student3=Registration("Ankit",22,9652358742,'O+')

student2.info()