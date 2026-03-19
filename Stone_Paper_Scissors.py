#Normal Logic 
'''
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
'''
import tkinter as tk
import random

# Global variables to keep track of scores
uscore = 0
cscore = 0

def play(user_choice):
    global uscore, cscore
    
    # Dictionary to map numbers to words for the display
    choices = {1: "Stone", 2: "Paper", 3: "Scissors"}
    com_choice = random.randint(1, 3)
    
    # Core logic from your script
    if (user_choice == 1 and com_choice == 3) or \
       (user_choice == 2 and com_choice == 1) or \
       (user_choice == 3 and com_choice == 2):
        uscore += 1
        round_result = f"You won the round!\nComputer chose {choices[com_choice]}."
    elif user_choice == com_choice:
        uscore += 1
        cscore += 1
        round_result = f"It was a draw!\nBoth chose {choices[com_choice]}."
    else:
        cscore += 1
        round_result = f"Computer won the round!\nComputer chose {choices[com_choice]}."
        
    # Update the score label
    score_label.config(text=f"You: {uscore}  |  Computer: {cscore}")
    
    # Check for game over (First to 5)
    if uscore >= 5 and cscore >= 5:
        status_label.config(text=round_result + "\n\nGAME OVER: It's a Tie Game!")
        disable_buttons()
    elif uscore >= 5:
        status_label.config(text=round_result + "\n\nGAME OVER: You Won this game!")
        disable_buttons()
    elif cscore >= 5:
        status_label.config(text=round_result + "\n\nGAME OVER: Computer Won this game!")
        disable_buttons()
    else:
        status_label.config(text=round_result)

def disable_buttons():
    # Turns off the buttons when the game finishes
    btn_stone.config(state=tk.DISABLED)
    btn_paper.config(state=tk.DISABLED)
    btn_scissors.config(state=tk.DISABLED)

# --- UI Setup ---
root = tk.Tk()
root.title("Stone, Paper, Scissors")
root.geometry("350x300")
root.eval('tk::PlaceWindow . center') # Centers the window

# Title Label
title_label = tk.Label(root, text="First to 5 Wins!", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=10)

# Buttons Frame (to put them side-by-side)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_stone = tk.Button(button_frame, text="Stone", width=8, command=lambda: play(1))
btn_stone.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(button_frame, text="Paper", width=8, command=lambda: play(2))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(button_frame, text="Scissors", width=8, command=lambda: play(3))
btn_scissors.grid(row=0, column=2, padx=5)

# Status Label (shows round results and game over)
status_label = tk.Label(root, text="Choose your weapon to start!", font=("Helvetica", 10), fg="blue")
status_label.pack(pady=20)

# Start the application
root.mainloop()       