import random

# Function to get a valid integer input
def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter a valid number.")

# Function to handle a single round of the game
def play_game():
    print("Let's start the guessing game!")

    # Get valid range values
    min_range = get_valid_integer("Enter the minimum number: ", -1000, 1000)
    max_range = get_valid_integer("Enter the maximum number: ", min_range + 1, 10000)

    # Generate the target number
    target_number = random.randint(min_range, max_range)

    # Initialize guess count and guess limit
    guess_count = 0
    guess_limit = 5

    # Start the guessing game loop
    while guess_count < guess_limit:
        guess = get_valid_integer("Enter your guess: ", min_range, max_range)
        guess_count += 1

        # Check if the guess is correct
        if guess == target_number:
            print(f"Correct! You guessed the number in {guess_count} attempts.")
            break
        elif guess < target_number:
            print("The number is higher. Try again.")
        else:
            print("The number is lower. Try again.")

    # If the max attempts are reached, notify the user
    if guess_count == guess_limit and guess != target_number:
        print(f"Sorry, you've used all {guess_limit} attempts. The correct number was {target_number}.")

# Main loop to ask if the user wants to play again
def main():
    while True:
        play_game()

        # Ask if the user wants to play again
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()

            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing! Visit us again!")
                exit()
            else:
                print("Invalid input. Please enter 'y' to continue or 'n' to exit.")

if __name__ == "__main__":
    main()
