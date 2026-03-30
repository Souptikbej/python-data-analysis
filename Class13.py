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
'''


#Display all distinct elements present in the given array
'''
a=[1,1,1,1,2,2,2,3,3,3,5,5,5,6,6,6,9,9,9,7,7,7,0]
d={}
for i in a:
  if i not in d.keys():
    c=a.count(i)
    d[i]=c
print(d.keys())
'''


#count frequency of Array Elements
'''
a=[1,1,1,1,2,2,2,3,3,3,5,5,5,6,6,6,9,9,9,7,7,7,0]
d={}
for i in a:
  if i not in d.keys():
    c=a.count(i)
    d[i]=c
print(d)
'''
#Compare character frequencies of two string and check if they match 
'''
s1="aabbcc"
s2="aaaccab"
if len(s1)==len(s2):
  dict1={}
  dict2={}

  for i in s1:
    dict1[i]=dict1.get(i,0)+1
  
  for i in s2:
    dict2[i]=dict2.get(i,0)+1
  
  print(dict1==dict2)
else:
  print("Not same")
'''
#Find Duplicate in array using hashset (Detect and print elements that appear more than once in the array)
'''
a=[2,5,7,9,3,5,6,2,5,6,3,1,3]
d={}
for i in a:
  d[i]=d.get(i,0)+1
for i in d:
  if d[i]>1:
    print(i)
'''
#Intersection of two array
'''
a=[1,2,2,1]
b=[2,2]
d={}
j=[]
for i in a:
  d[i]=d.get(i,0)+1
for i in d.keys():
  if i in b:
    j.append(i)
print(j)
'''
#Invert Dictionary
'''
d={'a': 10, 'b': 25, 'c': 20}
a={}
for i,j in d.items():
  a[j]=i
print(a)
'''
#Remove Emply and One Values
'''
d={'a': 1, 'b': None, 'c': '', 'd': 4}
for i in list(d.keys()):
  if d[i] is None or d[i]=='':
    del d[i]
print(d)
'''
