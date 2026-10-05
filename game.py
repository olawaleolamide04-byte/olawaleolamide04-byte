import random

computer_choice = 0
my_choice = 0

round_score = 3

game_choices = ["rock", "paper", "scissors"]

print("Welcome to our mini RSP game!!!")

while True:
    my_choice = input("Put in your choice in this list" + str(game_choices))
    computer_choice = random.choices(game_choices)

    print("You played" + "my_choice" + )