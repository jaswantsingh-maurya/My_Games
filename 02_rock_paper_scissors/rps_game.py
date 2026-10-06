import random 

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if user_choice == computer:
        print("It's a tie!")
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer == "paper"):
            print("You win!")
    else:
        print("You lose!")
