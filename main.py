from sys import path
from art import tprint

path.append("..\\packages")

from packages.calculate_modules.main_menu import menu


def main_menu():
    tprint("Calculator.")
    menu()


if __name__ == "__main__":
    print("[-- main.py-- was launched.]")
    main_menu()

else:
    print("[-- main.py-- was imported.]")
