import random

print("-" * 100)
print("Jak En Poy")
print("-" * 100)

choice = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("Choose: Rock, Paper, or Scissor ").title()
    comp_choice = random.choice(choice)
    print(f"\n You chose {user_choice}, computer chose {comp_choice}")

    if user_choice == comp_choice:
        print(f"Both players picked {user_choice}. Play Again")
    elif user_choice == "Rock":
        if comp_choice == "Scissor":
            print("You won")
        elif comp_choice == "Paper":
            print("You lost")
    elif user_choice == "Paper":
        if comp_choice == "Rock":
            print("You won")
        elif comp_choice == "Scissor":
            print("You lost")
    elif user_choice == "Rock":
        if comp_choice == "Scissor":
            print("You won")
        elif comp_choice == "Paper":
            print("You lost")
    play_again = input("Play again? (Y/N) ").upper()
    if play_again != "Y":
        break
