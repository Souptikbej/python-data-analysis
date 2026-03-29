'''
Concatenation X
Conversion
Cloning
Identity
Emptiness
Merging       X
Aliasing
Searching
Comparison    X

d={"Hello":100,"Bro":200,"Morning":300}

print(d["Bro"])#accessing the  value

d["Bro"]=500 #Change the value

print(d["Bro"])#Show  the  changed value

#Create dictionary first Way
d=dict(Name="Souptik Bej",Age=23,Gender="Male")
print(d)

#Create dictionary Second Way
d=dict([("Name","Souptik" ),("Age",23)])
print(d)


#Dictionary Trasversing
a={10:100,20:200,30:300}
for i in a:#1 ways values print using keys
  print(a[i])

for i in a.values():#2 ways values print
  print(i)

for i,j in a.items():#Key and value both print
  print(i,j)

for i in a.keys(): #Only print keys
  print(i)

#Enumerate() 
courses={'DAA':'CS','AOA':'ME','SVY':'CE'}
for i,(k,v) in enumerate(courses.items()):
  print(i,k)

#Reversed Dictionary using reversed()
courses={'DAA':'CS','AOA':'ME','SVY':'CE'}
for i,j in reversed(courses.items()):
  print(i,j)

'''
#Dictionary Methods
st={1:"Souptik",2:"Arnab",3:"Surya",4:"Ankit",5:"Rupam"}
St2={6:"Mansij",7:"Abhishak",8:"Goutam",9:"Indra",10:"Aliv"}

print(st.get(1,"Not Your List"))
print(st.get(11,"Not Your List"))

st.update(St2)
print(st)

print(st.popitem())        #Remove Key and value & Returns Key and value , Its Defults remove LIFO order
print(st)
print(st.pop(5))           #Remove key and value & returns its value
print(st)