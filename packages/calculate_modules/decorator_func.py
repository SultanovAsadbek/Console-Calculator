import time
from rich.console import Console
from rich.theme import Theme
from functools import wraps
from packages.calculate_modules.beatiful import success
from packages.calculate_modules.beatiful import get_data
from packages.calculate_modules.beatiful import clean_data
from packages.calculate_modules.beatiful import console


def decorate_func(func):
    """
    Описание:
        * Функция декоратор.
        * Функция принимает внешнюю функцию в качестве аргумента.
        * Декоратор добавляет заголовок соответственно с именем внешней функции.
        * Шрифт: жирный зелёный.

    Аргументы:
        func (function): внешняя функция.
    """

    @wraps(func)  # Не будет потреяться __name__ и __doc__ внешней функции.
    def wraper():
        if func.__name__ == "f_sum":
            console.print(f"\n{'-'*30} Сумма двух чисел {'-'*30}", style="bold yellow")
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "difference":
            console.print(
                f"\n{'-'*30} Разность двух чисел {'-'*30}\n", style="bold yellow"
            )
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "multiplication":
            console.print(
                f"\n{'-'*30} Умножение двух значений {'-'*30}\n", style="bold yellow"
            )
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "division":
            console.print(
                f"\n{'-'*30} Деление двух значений {'-'*30}\n", style="bold yellow"
            )
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "exponentiation":
            console.print(
                f"\n{'-'*30} Возведение в степень {'-'*30}\n", style="bold yellow"
            )
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "remainder":
            console.print(
                f"\n{'-'*30} Остаток от делений {'-'*30}\n", style="bold yellow"
            )
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "integer_division":
            console.print(
                f"\n{'-'*30} Целочисленные деление {'-'*30}\n", style="bold yellow"
            )
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "show_history":
            console.print(
                f"\n{'-'*30} Просмотр историй {'-'*30}\n", style="bold yellow"
            )
            get_data()
            func()
            console.print(f"{'-'*80}\n", style="bold yellow")
            time.sleep(2)

        if func.__name__ == "clean_history":
            console.print(f"\n{'-'*30} Очистка историй {'-'*30}\n", style="bold yellow")
            clean_data()
            func()
            console.print("Очищения прошла успешно!", style="bold underline green")
            console.print(f"{'-'*80}\n", style="bold yellow")

    return wraper
