import random
cscore=0
uscore=0

while True:
  print(f"Current Scores\nYou - {uscore}\nComputer - {cscore}\n")
  user = int(input("1 for stone , 2 for paper , 3 fro scissors choose :- "))
  com=random.randint(1,3)
  if user==1 and com==3:
    uscore+=1
    print("You won the Round\n")
  elif user==2 and com==1:
    uscore+=1
    print("You won the Round\n")
  elif user==3 and com==2:
    uscore+=1
    print("You won the Round\n")
  elif user==com:
    uscore+=1
    cscore+=1
    print("It was a draw")
  else:
    cscore+=1
    print("Computer won the Round\n")
  if cscore==5:
    print("Game Over Computer Won this game")
    break
  elif uscore==5:
    print("Game Over You Won this game")
    break