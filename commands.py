import sys
from terminaltexteffects.effects.effect_wipe import Wipe
from users import User, new_user, find_user, calculate
from enum import Enum


def start():
    # Create a Wipe effect instance with the given word
    effect = Wipe(
        "Macro-Micro-Calc calculates the recommended macros a person should consume\nbased on the persons age, weight, height, sex, and activity level.\nAlso based on user input, receive a list of DRIs for vitamins and minerals.\nLet's get started!"
    )
    # Use the effect's terminal output context
    with effect.terminal_output() as terminal:
        # Print each frame of the animation
        for frame in effect:
            terminal.print(frame)
    user = find_user()
    if user == None:
        user = new_user()
    else:
        print(f"Welcome back, {user.name}!")
    prompt(user)


def prompt(user):
    calculate(user)
    user.print_info()
    command = input(f"{user.name} -> ")
    match command:
        case "login":
            print("Switching users....")
            user = new_user()
        case "update":
            print("Update user info. Not implemented yet.")
        case "help":
            print("Usage:")
            print("- login: login to specific user.")
            print("- update: update users info")
            print("- exit: exit program.")
            print("- help: displays a list of all available commands.")
        case "exit":
            handle_exit()
        case _:
            print("Unknown command. Try 'help' for a list of commands.")

    prompt(user)


def handle_exit():
    print("Goodbye!")
    sys.exit(0)
