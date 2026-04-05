class Factory:
  a="hello i am an attribute"
  def hello(s):
    print("Hello i am a method")
 
obj=Factory()#obj became an object who can access anything inside the class till now
obj2=Factory()
print(obj.a)
obj2.hello() 