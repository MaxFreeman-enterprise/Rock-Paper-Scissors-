import random
from enum import Enum

PAPER = "paper"
SCISSORS = "scissors"
ROCK = "rock"
DRAW_SCORE = 50
WIN_SCORE = 100
DEFAULT_GAME_OPTIONS = ["paper", "scissors", "rock"]


class GameResults(Enum):
    USER = 1
    PC = 2
    DRAW = 3


def who_wins(user_choice, pc_choice, game_options):
    if user_choice in user_game_options and pc_choice == user_choice:
        return GameResults.DRAW
    else:
        user_choice_options_index = game_options.index(user_choice)
        options_rated_for_user_choice = game_options[user_choice_options_index + 1:] + game_options[
                                                                                       :user_choice_options_index]
        if options_rated_for_user_choice.index(pc_choice) > len(
                options_rated_for_user_choice) // 2 - 1:  # for an even len(game_options) less pc choices win over a given user choice
            return GameResults.USER
        else:
            return GameResults.PC


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
rating_file = open("rating.txt", mode="r")
current_user_rating = 0
for line in rating_file:
    if line.split()[0] == user_name:
        current_user_rating = int(line.split()[1])

user_game_options = input().split(",")

if user_game_options == [""]:
    user_game_options = DEFAULT_GAME_OPTIONS

print("Okay, let's start")

while True:

    pc_choice = random.choice(user_game_options)

    user_choice = input()

    if user_choice == "!rating":
        print(f"Your rating: {current_user_rating}")

    elif user_choice in user_game_options:
        winner = who_wins(user_choice, pc_choice, user_game_options)
        if winner == GameResults.USER:
            current_user_rating += WIN_SCORE
            print(f"Well done. The computer chose {pc_choice} and failed")

        elif winner == GameResults.PC:
            print(f"Sorry, but the computer chose {pc_choice}")

        else:
            print(f"There is a draw {pc_choice}")
            current_user_rating += DRAW_SCORE

    elif user_choice == "!exit":
        print("Bye!")
        break

    else:
        print("Invalid input")
rating_file.close()
