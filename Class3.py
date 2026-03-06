a= "Hello I am Data Scientist"

#Extract Hello
print(a[0:5:1])
#Extract Data
print(a[11:16:1])
#Extract Scientist
print(a[16::1])


print(ord('A'))


age=23
name="souptik"

print(name[7::-1])
print(f"My name is\t{name} and \n\tage is\t{age}")


x=50.6
print(str(x))
print("Hello".lower())

print("sheryians".count("i"))


a="Souptik"
print(len(a))

b=" Bej"
print(a+b)


arr = [0] * 5
for i in range(5):
    print(str(arr[i]) + " ")



a=input("Enetr the string : ")
n=len(a)
print(a[n::-1])


print("123".isdigit())