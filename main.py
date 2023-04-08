import random

print("-" * 100)
print("Jak En Poy")
print("-" * 100)


def computer_action():
    choice = ["Rock", "Paper", "Scissor"]
    comp_choice = random.choice(choice)
    return comp_choice


def winner(user_choice, comp_choice):
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


while True:
    user_choice_1 = input("Choose: Rock, Paper, Scissor: ").title()
    comp = computer_action()
    print(f"You choose {user_choice_1}, computer choose {comp}")
    winner(user_choice_1, comp)

    play_again = input("Play again? (Y/N) ").upper()
    if play_again != "Y":
        break
