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
'''
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)-1):
  a[i],a[i+1]=a[i+1],a[i]
print(a)
'''
#Right Rotation by 1
'''
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)-1,0,-1):
  a[i],a[i-1]=a[i-1],a[i]
print(a)
'''
#K times rotation 
'''
k=int(input("Enter how many time u wants to rotate : "))
a=[10,20,30,40,50,60,70,80,90,100]
print(f"Before Rotation List Looks Like : {a}")
for j in range(1,k+1):
  for i in range(len(a)-1):
    a[i],a[i+1]=a[i+1],a[i]
  print(f"{j} time rotation looks : {a}")
'''
#Reverse the entire list without using extra space 
'''
a=[10,20,30,40,50,60,70,80,90]
print(f"Before Rotation List Looks Like : {a}")
l=len(a)-1
for i in range(len(a)//2):
  a[i],a[l]=a[l],a[i]
  l-=1
print(f"After Rotation List Looks Like : {a}")
'''
#Linear Search
'''
a=[1,25,32,96,35,74,55,66,38,94,50]
search=35
for i in range(len(a)):
  if search==a[i]:
    print(f"Element found at index of {i}")
    break
else:
  print("Element Not Found")
'''
#Binary Search
'''
a=[10,20,30,40,50,60,70,80,90]
search=40
start=0
last=len(a)-1
while start<=last:
  mid=(start+last)//2
  if a[mid]==search:
    print(f"Elememt Found at index {mid}")
    break
  elif a[mid]>search:
    last=mid-1
  elif a[mid]<search:
    start=mid+1
else:
  print("Not found")
'''
#Bubble Sort
'''
a=[34,26,89,123,18,12,11]
for j in range(len(a)-1):
  for i in range(len(a)-1-j):
    if a[i]>a[i+1]:
      a[i],a[i+1]=a[i+1],a[i]
print(f"Bubble Sort : {a}")
'''
#Selection Sort
a=[34,26,89,123,18,12,11]
for i in range(len(a)-1):
  j=i+1
  min=i
  for k in range(j,len(a)):
    if a[k]<a[min]:
      min=k
  a[i],a[min]=a[min],a[i]
print(f"Selection Sort : {a}")