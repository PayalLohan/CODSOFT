

import random

def get_user_choice():
    """Prompts the user to choose rock, paper, or scissors and validates input."""
    while True:
        user_input = input("Choose your move (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generates a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on user's and computer's choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Plays a single round of Rock-Paper-Scissors."""
    print("\n--- Rock-Paper-Scissors Game ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result # Return the result for score tracking

def main():
    """Main function to run the Rock-Paper-Scissors game with score tracking and play again option."""
    user_score = 0
    computer_score = 0

    while True:
        game_result = play_game()

        if game_result == "You win!":
            user_score += 1
        elif game_result == "Computer wins!":
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()