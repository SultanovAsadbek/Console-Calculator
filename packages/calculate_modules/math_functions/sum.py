import time
from packages.calculate_modules.beatiful import console
from packages.calculate_modules.beatiful import success
from packages.calculate_modules.beatiful import display_status
from packages.calculate_modules.decorator_func import decorate_func
from packages.calculate_modules.history import cursor
from packages.calculate_modules.history import connection


@decorate_func
def f_sum():
    """
    Описание:
        * Целочисленное деление двух чисел.
        * Функция получает от пользователя два числа и
            выведет на экран красивый результат вычислений.

    Аргументы:
        * Не принимаент аргументов.

    """

    # Ввод с клавиатуры.
    value_1 = input("значение 1: ")
    value_2 = input("значение 2: ")

    # Действия функций --display_status()-- :
    # Если в введённом данных будут присутствовать символы кроме числы...
    # индикатор выполнения --> выведется сообщения об ошибке --> прерывается функция --f_sum()--.
    display_status(value_1, value_2)

    # При успешном ввод данных...
    # --success()-- выведет индикатор выполнения.
    success()

    # Вычисления операций.
    # Округление до двух значений после точки.
    decision = float(value_1) + float(value_2)

    # Красивый вывод на экран:
    # в жирном подчеркнутом зеленом шрифте.
    console.print(f"{value_1} + {value_2} = {decision}", style="bold underline green")

    # ----------- Сохранение в базы данных -----------

    # Группировка данных в список.
    values = [
        value_1,
        value_2,
        "Сумма двух значений.",
        decision,
        time.strftime("%d.%m.%Y"),
        time.strftime("%H:%M:%S"),
    ]

    # Преобразовать в кортеж, так как файл recently_operations.db принимает кортеж для записи данных.
    cursor.execute(
        """INSERT INTO history_decisions(value_1, value_2, operation, decision, date, time) VALUES(?, ?, ?, ?, ?, ?)""",
        tuple(values),
    )

    # Запись в файл recently_operations.db (База данных).
    connection.commit()


if __name__ == "__main__":
    print("--| sum.py |-- was launched.")

else:
    print("--| sum.py |-- was imported.")
