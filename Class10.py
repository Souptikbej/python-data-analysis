#Sum & Avg of a list
'''
a=[10,20,30,40,50]
s=0
for i in range(len(a)):
  s=s+a[i]
print(f"Sum of number of a list : {s}")
print(f"Average of your list numbers are {s/len(a)}")
'''
#Maximum Element with index
'''
a=[10,20,30,40,50]
m=0
index=0
for i in range(len(a)):
  if a[i]>m:
    m=a[i]
    index+=1
print(f"Maximum Element is {m} and index is {index}")
'''
#Second Grestest Element
'''
a=[10,20,30,40,50,45]
m=0
m2=0
index=0
index2=0
for i in range(len(a)):
  if a[i]>m:
    m2=m
    m=a[i]
    index2=index
    index=i
  elif a[i]>m2:
    m2=a[i]
    index2=i
print(f"Second Maximum Element is {m2} and index is {index2}")
'''
#Check if List is Sorted (Increasing)
'''
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)-1):
  if a[i]< a[i+1]:
    continue
  else:
    print("List is not sorted")
    break
else:
  print("list is sorted")
'''
#Left Rotation by 1
