"""  Please make sure you read the entire README.md file to follow the instructions.
You dont have to follow how I have started the game. Please use your creativity """
    
import random

def guess_the_number():
    # Randomly choose a number between 1 and 10
    secret_number = random.randint(1, 10)
    guess = 0
    count = 0
   

    print("\nWelcome to Number Guessing Game!")
    print("Guess a number between 1 & 10")

    while True:
        # Ask the user to enter their guess
        user_input = input("\nGuess the number: ") 
        count += 1

        # Ensure an input is an integer
        if user_input.isdigit():
            guess = int(user_input)
            
     # Compare the guess to the secret number
            if guess < secret_number:
             print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {count} count(s).")
                break  # Exit the loop when the guess is correct
        else:
            print("Enter a valid number.")

    # Ask the user for replay
    play_again = input("Do you wish to continue the Game? (yes/no): ")
    if play_again == "yes":
        guess_the_number()
    else:
        print("\nThanks for playing! Goodbye!\n")

# Start the game again
guess_the_number()