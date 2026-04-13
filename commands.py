import sys
from terminaltexteffects.effects.effect_wipe import Wipe
from users import User
from enum import Enum


def start():
  # Create a Wipe effect instance with the given word
  effect = Wipe("Macro-Micro-Calc calculates the recommended macros a person should consume\nbased on the persons age, weight, height, sex, and activity level.\nAlso based on user input, receive a list of DRIs for vitamins and minerals.\nLet's get started!")
  # Use the effect's terminal output context
  with effect.terminal_output() as terminal:
      # Print each frame of the animation
      for frame in effect:
          terminal.print(frame)
  name = input("Enter name -> ")
  user = User(name)
  print(f"Welcome, {user.name}! Let's find your info!")
  prompt(user)


def prompt(user):
  command = input(f"{user.name} -> ")
  match (command):
    case "login":
      print("Not implemented yet")
    case "help":
      print("Usage:")
      print("- login: login to specific user.")
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