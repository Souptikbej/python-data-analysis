import random
num=random.randint(1,100)
tries=0
while True:
  guessed= int(input("Guessed the number between 1 to 100 : "))
  tries+=1
  if guessed == num :
    print(f"Congratulations you found yopu number in {tries} tries")
    break
  elif guessed > num :
    print("Sorry you need to go lower")
  elif guessed < num :
    print("Sorry you have to go a littel upper")
  else:
    print("Sorry put number behave the rules...")