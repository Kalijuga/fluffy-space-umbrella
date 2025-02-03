import random

user_action = input("Enter a choice (Stein, Papier, Schere): ").strip().lower()
possible_actions = ["Stein", "Papier", "schere"]
computer_action = random.choice(possible_actions)
print(f"Du hast {user_action} gewählt, der Computer hat {computer_action}.\n")


if user_action == computer_action:
    print("Unentschieden")
if user_action == "stein":
    if computer_action == "schere":
        print(f"Gewonnen, computer: {computer_action}.")
    else:
        print(f"Verlohren, computer: {computer_action}.")
elif user_action == "papier":
    if computer_action == "stein":
        print(f"Gewonnen, computer: {computer_action}.")
    else:
        print(f"Verlohren, computer: {computer_action}.")
elif user_action == "schere":
    if computer_action == "papier":
        print(f"Gewonnen, computer: {computer_action}.")
    else:
        print(f"Verlohren, computer: {computer_action}.")