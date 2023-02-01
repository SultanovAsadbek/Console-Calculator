from packages.calculate_modules.math_functions.difference import difference
from packages.calculate_modules.math_functions.division import division
from packages.calculate_modules.math_functions.exponentiation import exponentiation
from packages.calculate_modules.math_functions.integer_division import integer_division
from packages.calculate_modules.math_functions.multiplication import multiplication
from packages.calculate_modules.math_functions.remainder import remainder
from packages.calculate_modules.math_functions.sum import f_sum
from packages.calculate_modules.exeptions import TypeExc

from packages.calculate_modules.beatiful import console
from packages.calculate_modules.beatiful import finish_programm
from packages.calculate_modules.history import cursor
from packages.calculate_modules.history import connection
from packages.calculate_modules.history import show_history
from packages.calculate_modules.history import clean_history


def controller(command):
    """
    * В функции вызывается все функции из папки --packages/calculate_modules/math_functions---
    * Функция вызывает функцию
        по соответствующим командам.

    Аргументы:
    --------------------
    command (str): команды полученные от пользователя.

    """

    if command == "1":
        try:
            f_sum()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "2":
        try:
            difference()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "3":
        try:
            multiplication()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "4":
        try:
            division()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "5":
        try:
            exponentiation()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "6":
        try:
            remainder()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "7":
        try:
            integer_division()
        except TypeExc as error:
            console.print(error, style="bold underline red")
            console.print(f"{'-'*78}\n", style="bold yellow")

    elif command == "8":
        show_history()

    elif command == "9":
        clean_history()

    elif command in ("exit", "0"):
        cursor.close()
        connection.close()
        finish_programm()
        return False

    else:
        console.print("Команда не найдена!", style="bold underline red")
