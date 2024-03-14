import random

human_choice = input("Enter your choice (rock, paper, scissors): ")

computer_choice = random.choice(["rock", "paper", "scissors"])



print(f"You chose {human_choice}, computer chose {computer_choice}.")

if human_choice == computer_choice:
  print("It's a tie!")
  print("-------------")
  print("-------------")
  print("-------------")
  print("-------------")
elif human_choice == "rock" and computer_choice == "paper":
  print("Computer wins!")
elif human_choice == "scissors" and computer_choice == "paper":
  print("You win!")
else:
  print("Invalid input. Please enter either rock, paper, or scissors.")