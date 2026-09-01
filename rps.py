#Rock paper scissors game
import random
choices = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(choices)
    player_choice = input("Please enter your choice (rock/paper/scissors): ").strip().lower()
    while player_choice not in choices:
        print("Invalid choice. Please try again.")
        player_choice = input("Please enter your choice (rock/paper/scissors): ").strip().lower()
    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    continue_playing = input("Do you want to play again? (yes/no): ").strip().lower()
    if continue_playing == "no":
        print("Thanks for playing!")
        break

    