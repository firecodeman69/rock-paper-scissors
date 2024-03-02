# Rock, Paper, Scissors game.
# The first to win 5 times wins!

import utility
import cv2
from random import choice

# Mapping hands to numbers
hands = {"rock": 0, "paper": 1, "scissors": 2}

computer_score = 0
player_score = 0
winning_score = 5

def play_game():
    while True:
        print("The computer is picking a hand!")
        computer_hand = choice(list(hands.keys()))
        print("The computer has made their choice. Get ready to take a photo of your choice!")

        print("Now it's your turn. Hold up your choice to the camera")
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        capture.release()
        cv2.imwrite("playerchoice.jpg", frame)

        player_hand = utility.determine_hand("playerchoice.jpg").strip()  
        # Remove leading and trailing whitespace
        print(f"You chose: {player_hand}.\nComputer's hand is: {computer_hand}")

        # Mapping hands to numbers
        computer_num = hands[computer_hand]
        player_num = hands[player_hand]

        # Compare choices
        if (player_num - computer_num) % 3 == 1:
            print("You win!")
            player_score += 1
        elif (player_num - computer_num) % 3 == 2:
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Scores: Player - {player_score}, Computer - {computer_score}")

        # Check if either player has won 3 times
        if player_score == winning_score:
            print("Congratulations! You won!")
            break
        elif computer_score == winning_score:
            print("Computer won. Better luck next time!")
            break