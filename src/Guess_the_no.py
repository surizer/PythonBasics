import random

def play_game():
    print("Lets start the guessing game")
    min_range = int(input("Enter the minimum number:"))
    max_range = int(input("Enter the minimum number:"))
    #Generate a random number between 1 and 100.
    target_number = random.randint(min_range, max_range)

    #initalise guess count and no of guess a user can have.
    guess_count = 0
    guess_limit = 5

    #The guessing game starts here.
    while guess_count < guess_limit:
        try:
            #Ask for the users input.
            guess =int(input("Enter your guess:"))
        except ValueError:
            print("Please enter a valid no")
            continue

        guess_count += 1

        #Check if the guess is correct.
        if guess == target_number:
            print(f" Correct! you guessed the number in {guess_count} attempts. ")
            break #Exit the loop as the guess was correct.
        elif guess < target_number:
            print("Lower than the actual number")
        else:
            print("Higher than the actual number")
    #If the max guess has reached and user has not guessed the number correctly, exit smoothly.
    if guess_count == guess_limit and guess != target_number:
        print(f"Sorry you have reached the max attempts{guess_limit}. The correct number was {target_number}")

while True:
    play_game()

    #Ask if the user wants to play again
    while True:
        play_again=input("Do you want to play again?(y/n)").lower()

        if play_again in ['yes','y']:
            break
        elif play_again in ['no','n']:
            print("Thanks for playing! Visit us again!")
            exit()
        else:
            print("Invalid input, please enter 'y' to continue or 'n' to exit.")

