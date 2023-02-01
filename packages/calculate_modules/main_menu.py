from packages.calculate_modules.menu_controller import controller
from packages.calculate_modules.beatiful import console


def menu():
    """
    * Функция не имеет параметров.
    * Функция предоставляет пользователю меню команд,
        полученную команду передаёт
    в функцию [-- controller() --] в качестве аргумента.

    Ключевые аргументы:
    -------------------
    аргументы отсутствуют.

    Возврат:
    ------------
    False
        При завершении работы

    """
    while True:
        console.print(
            f"""
{'-' * 50}
[1]:  Сумма.
[2]:  Разность.
[3]:  Умножение.
[4]:  Деление.
[5]:  Возведение в степени.
[6]:  Остаток от делении.
[7]:  Целочисленное деление.

Недавно решённые задачи:
------------------------
[8]: Просмотр историй.
[9]: Очистка историй.
------------------------ 

[0/exit]: Выход из программы.
{'-' * 50}
        """,
            style="bold cyan",
        )

        operation = input("Выберите операцию: ").strip().lower()  # Ввод с клавиатуры.
        
        if operation in ("0", "exit"):
            controller(operation)
            return False

        controller(operation)
