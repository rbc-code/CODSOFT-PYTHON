import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"
def play_round():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return None, None
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")
    return winner, user_choice
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    while True:
        print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}")
        winner, _ = play_round()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        play_again = input("Do you want to play another round? (yes/no): ").lower().strip()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
if __name__ == "__main__":
    rock_paper_scissors()
