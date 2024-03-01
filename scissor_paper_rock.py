from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox
import time
import os
import sys

# Check the operating system
if sys.platform.startswith('win'):
    import winsound

# Main window
root = Tk()
root.title("Rock Scissors Paper")
root.configure(background="#9b59b6")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# Load sounds
rock_sound = os.path.join("sounds", "rock.wav")
paper_sound = os.path.join("sounds", "paper.wav")
scissor_sound = os.path.join("sounds", "scissors2.wav")
win_sound = os.path.join("sounds", "win.wav")
lose_sound = os.path.join("sounds", "lose.wav")

# Insert images
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
player_score = 0
computer_score = 0

# Indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# Update message
def update_message(message):
    msg['text'] = message

# update user score
def update_user_score():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def update_comp_score():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

'''
# Update user score
def update_user_score():
    global player_score
    player_score += 1
    playerScore.config(text=str(player_score))

# Update computer score
def update_comp_score():
    global computer_score
    computer_score += 1
    computerScore.config(text=str(computer_score))
'''

# Check winner
def check_win(player, computer):
    if player == computer:
        update_message("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            update_message("You lose")
            update_comp_score()
            root.after(500, lambda: [update_message(""),
                                     play_sound(lose_sound)])
        else:
            update_message("You win")
            update_user_score()
            root.after(500, lambda: [update_message(""),
                                     play_sound(win_sound)])
    elif player == "paper":
        if computer == "scissors":
            update_message("You lose")
            update_comp_score()
            root.after(500, lambda: [update_message(""),
                                     play_sound(lose_sound)])
        else:
            update_message("You win")
            update_user_score()
            root.after(500, lambda: [update_message(""),
                                     play_sound(win_sound)])
    elif player == "scissors":
        if computer == "rock":
            update_message("You lose")
            update_comp_score()
            root.after(500, lambda: [update_message(""),
                                     play_sound(lose_sound)])
        else:
            update_message("You win")
            update_user_score()
            root.after(500, lambda: [update_message(""),
                                     play_sound(win_sound)])

# Play sound
def play_sound(sound_file):
    if sys.platform.startswith('win'):
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif sys.platform.startswith('darwin'):
        os.system("afplay '{}'".format(sound_file))
    else:
        print("Unsupported platform for playing sound")

# Update choices
choices = ["rock", "paper", "scissors"]
def update_choice(user_choice):
    # Play sound based on user choice
    if user_choice == "rock":
        play_sound(rock_sound)
    elif user_choice == "paper":
        play_sound(paper_sound)
    elif user_choice == "scissors":
        play_sound(scissor_sound)

    # Computer's choice
    comp_choice = choices[randint(0, 2)]
    if comp_choice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # User's choice
    if user_choice == "rock":
        user_label.configure(image=rock_img)
    elif user_choice == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    check_win(user_choice, comp_choice)

# Buttons
def show_instructions():
    messagebox.showinfo("Instructions", "Welcome to Rock, Paper, Scissors game!\n\nClick on one of the buttons to choose your move: Rock, Paper, or Scissors.\nThe computer will randomly choose its move. The winner will be determined based on the rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n\nHave fun and good luck!")

def show_hint():
    messagebox.showinfo("Hint", "Choose your move wisely! Try to anticipate the computer's move based on patterns.")

rock = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D", fg="white", command=lambda: update_choice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="Paper", bg="#FAD02E", fg="white", command=lambda: update_choice("paper")).grid(row=2, column=2)
scissors = Button(root, width=20, height=2, text="Scissors", bg="#0ABDE3", fg="white", command=lambda: update_choice("scissors")).grid(row=2, column=3)

# Instructions and hints buttons
instructions_button = Button(root, text="Instructions", command=show_instructions).grid(row=4, column=4, columnspan=2)
hint_button = Button(root, text="Hint", command=show_hint).grid(row=4, column=5, columnspan=2)

# Scores
playerScore = Label(root, text="0", font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text="0", font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Function to start a new game
def new_game():
    # Reset scores
    playerScore.config(text="0")
    computerScore.config(text="0")

    # Reset player and computer images
    user_label.configure(image=scissor_img)
    comp_label.configure(image=scissor_img_comp)

    # Reset message
    update_message("")

    # Enable player choice buttons
    rock.config(state="normal")
    paper.config(state="normal")
    scissors.config(state="normal")

# Buttons for new game and exit
new_game_button = Button(root, text="New Game", command=new_game).grid(row=4, column=2)
exit_button = Button(root, text="Exit", command=root.quit).grid(row=4, column=3)

root.mainloop()
