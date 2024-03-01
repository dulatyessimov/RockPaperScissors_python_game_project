from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import sys
import pygame

# Initialize pygame
pygame.mixer.init()

# Main window
root = Tk()
root.title("Rock Scissors Paper")
root.configure(background="#9b59b6")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))

# Load sounds
rock_sound = pygame.mixer.Sound(os.path.join("sounds", "rock.wav"))
paper_sound = pygame.mixer.Sound(os.path.join("sounds", "paper.wav"))
scissor_sound = pygame.mixer.Sound(os.path.join("sounds", "scissors2.wav"))
win_sound = pygame.mixer.Sound(os.path.join("sounds", "win.wav"))
lose_sound = pygame.mixer.Sound(os.path.join("sounds", "lose.wav"))

# Scores
player1_score = 0
player2_score = 0

# Indicators
player1_indicator = Label(root, font=50, text="PLAYER 1", bg="#9b59b6", fg="white")
player2_indicator = Label(root, font=50, text="PLAYER 2", bg="#9b59b6", fg="white")
player1_indicator.grid(row=0, column=1)
player2_indicator.grid(row=0, column=3)

# Messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# Update message
def update_message(message):
    msg['text'] = message

# update player1 score
def update_player1_score():
    score = int(player1Score["text"])
    score += 1
    player1Score["text"] = str(score)

# update player2 score
def update_player2_score():
    score = int(player2Score["text"])
    score += 1
    player2Score["text"] = str(score)

# Play sound effect based on choice
def play_sound(choice):
    if choice == "rock":
        rock_sound.play()
    elif choice == "paper":
        paper_sound.play()
    elif choice == "scissors":
        scissor_sound.play()

# Check winner
def check_win(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        update_message("It's a tie!")
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        update_message("Player 1 wins!")
        update_player1_score()
        win_sound.play()
    else:
        update_message("Player 2 wins!")
        update_player2_score()
        win_sound.play()

# Update choices
def update_choice(player, choice):
    if player == 1:
        if choice == "rock":
            player1_label.configure(image=rock_img)
        elif choice == "paper":
            player1_label.configure(image=paper_img)
        elif choice == "scissors":
            player1_label.configure(image=scissor_img)
    else:
        if choice == "rock":
            player2_label.configure(image=rock_img)
        elif choice == "paper":
            player2_label.configure(image=paper_img)
        elif choice == "scissors":
            player2_label.configure(image=scissor_img)

# Buttons
def choose_option(player, choice):
    update_choice(player, choice)
    play_sound(choice)
    if player == 1:
        player1_choice.set(choice)
        player2_button_rock.config(state="normal")
        player2_button_paper.config(state="normal")
        player2_button_scissors.config(state="normal")
        player1_button_rock.config(state="disabled")
        player1_button_paper.config(state="disabled")
        player1_button_scissors.config(state="disabled")
    else:
        player2_choice.set(choice)
        update_choice(player, choice)  # Update choice for player 2
        check_win(player1_choice.get(), player2_choice.get())
        player1_label.grid(row=1, column=0)
        player2_label.grid(row=1, column=4)  # Add this line to place player 2's choice in the layout
        player2_button_rock.config(state="disabled")
        player2_button_paper.config(state="disabled")
        player2_button_scissors.config(state="disabled")

# Function to start a new game
def new_game():
    player1_label.grid_remove()
    player1_label.configure(image="")
    player2_label.configure(image="")
    player1_choice.set("")
    player2_choice.set("")
    update_message("")
    player1_button_rock.config(state="normal")
    player1_button_paper.config(state="normal")
    player1_button_scissors.config(state="normal")
    player2_button_rock.config(state="disabled")
    player2_button_paper.config(state="disabled")
    player2_button_scissors.config(state="disabled")

# Buttons
player1_button_rock = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D", fg="white", command=lambda: choose_option(1, "rock"))
player1_button_rock.grid(row=2, column=0)
player1_button_paper = Button(root, width=20, height=2, text="Paper", bg="#FAD02E", fg="white", command=lambda: choose_option(1, "paper"))
player1_button_paper.grid(row=2, column=1)
player1_button_scissors = Button(root, width=20, height=2, text="Scissors", bg="#0ABDE3", fg="white", command=lambda: choose_option(1, "scissors"))
player1_button_scissors.grid(row=2, column=2)

player2_button_rock = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D", fg="white", command=lambda: choose_option(2, "rock"), state="disabled")
player2_button_rock.grid(row=2, column=3)
player2_button_paper = Button(root, width=20, height=2, text="Paper", bg="#FAD02E", fg="white", command=lambda: choose_option(2, "paper"), state="disabled")
player2_button_paper.grid(row=2, column=4)
player2_button_scissors = Button(root, width=20, height=2, text="Scissors", bg="#0ABDE3", fg="white", command=lambda: choose_option(2, "scissors"), state="disabled")
player2_button_scissors.grid(row=2, column=5)

# Scores
player1Score = Label(root, text="0", font=100, bg="#9b59b6", fg="white")
player2Score = Label(root, text="0", font=100, bg="#9b59b6", fg="white")
player1Score.grid(row=1, column=1)
player2Score.grid(row=1, column=3)

# Labels to display choices
player1_label = Label(root, bg="#9b59b6")
player2_label = Label(root, bg="#9b59b6")

# Choices of players
player1_choice = StringVar()
player2_choice = StringVar()

# Buttons for new game and exit
new_game_button = Button(root, text="New Game", command=new_game).grid(row=4, column=2)
exit_button = Button(root, text="Exit", command=root.quit).grid(row=4, column=3)

root.mainloop()
