from rich.progress import track
from time import sleep
from packages.calculate_modules.exeptions import TypeExc
from rich.console import Console
from rich.theme import Theme

console = Console()


def failed():
    """
    Описание:
        * Индикатор выполнения.
        * Функция вызывается при не удачном выполнении операции.

    Аргументы:
        * Функция не принимает аргументов на вход.
    """

    # Индикатор выполнения красного цвета означающего не корректность.
    for _ in track(range(100), description="[red]Обнаружение ошибок."):
        sleep(0.02)


def success():
    """
    Описание:
        * Индикатор выполнения.
        * Функция вызывается при успешном выполнении операции.

    Аргументы:
        * Функция не принимает аргументов на вход.
    """

    # Индикатор выполнения зелёного цвета означающего корректность.
    for _ in track(range(100), description="[green]Задача в процессе решения."):
        sleep(0.02)


def finish_programm():
    """
    Описание:
        * Индикатор выполнения.
        * Функция вызывается при выходе из программы.

    Аргументы:
        * Функция не принимает аргументов на вход.
    """

    # Индикатор выполнения жёлтого цвета означающего выход из программы.
    for _ in track(range(100), description="[yellow]Завершение программы."):
        sleep(0.02)


def get_data():
    """
    Описание:
        * Индикатор выполнения.
        * Функция вызывается при получений данных из БД.

    Аргументы:
        * Функция не принимает аргументов на вход.
    """

    # Индикатор выполнения жёлтого цвета означающего выход из программы.
    for _ in track(range(100), description="[cyan]Истории извлекаются."):
        sleep(0.02)


def clean_data():
    """
    Описание:
        * Индикатор выполнения.
        * Функция вызывается при удалений данных из БД.

    Аргументы:
        * Функция не принимает аргументов на вход.
    """

    # Индикатор выполнения жёлтого цвета означающего выход из программы.
    for _ in track(range(100), description="[cyan]Истории очищаются."):
        sleep(0.02)


def display_status(arg1, arg2):
    """
    Описание:
        * Функция проверяет корректность введённых данных.
        * Если в введённом данных будут присутствовать символы кроме числы...
            индикатор выполнения --> вызывается класс исключение --TypeExc-- --> прерывается функция --division()--.

    Аргументы:
        arg1 (_literal_): аргумент получаются из функции.
        arg2 (_literal_): аргумент получаются из функции.

    Raises:
        TypeExc: Класс исключение, вызывается если в введённом данных будут присутствовать символы кроме числы
                 с сообщением, затем прерывается программа
    """

    if arg1.isalpha() == True or len(arg1) == 0:
        failed()
        raise TypeExc(message="Введите числа!")

    if arg2.isalpha() == True or len(arg2) == 0:
        failed()
        raise TypeExc(message="Введите числа!")