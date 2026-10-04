import random

def play_game():
    game_over = False

    print("I am thinking of a no. from 1 to 100.")
    number = random.randint(1,100)

    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("Error")
        return

    while not game_over:
        print(f"You have {lives} turns remaining to guess the no.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Yay! You have guessed the correct no.")
            game_over = True
        elif guess > number:
            print("Too high.")
            lives -= 1
        else:
            print("Too low.")
            lives -= 1

        if lives == 0:
            game_over = True
            print("Oh no! You lost all of your chances of guessing.")

    again = input("Do you wanna play again? Type 'y' for yes and 'n' for no.")
    if again == "y":
        print("\n"*20)
        play_game()

play = input("Do you wanna play the game of guessing the no.? Type 'y' for yes and 'n' for no.")
if play == "y":
    play_game()