import sqlite3
from rich.console import Console
from rich.table import Table
from packages.calculate_modules.decorator_func import decorate_func


try:
    # Соединение с БД.
    connection = sqlite3.connect("recently_operations.db")
    cursor = connection.cursor()

except sqlite3.DatabaseError as error:
    # Вывод конкретных ошыбок.
    print(error)

else:
    #  SQLITE запрос на создание таблицы в файле recently_operations.db
    #  Создать таблицу если таблица не создана.
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS history_decisions(
        value_1 REAL,
        value_2 REAL,
        operation TEXT,
        decision REAL,
        date TEXT,
        time TEXT        
        )"""
    )


@decorate_func
def show_history():
    """
    Описание:
        * Функция отвечает за вывод на экран все данные из файла recently_operations.db (База данных)
        * Функция выводит на экран данные в виде таблицы:
        ┏━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
        ┃ X   ┃ Y    ┃ Операция              ┃ Решения ┃ Дата       ┃ Время    ┃
        ┡━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
        │ 12  │ 34   │ Сумма двух значений.  │ 46      │ 01.02.2023 │ 01:00:21 │
        │ 123 │ 34.3 │ Деление двух значений │ 3.59    │ 01.02.2023 │ 01:00:40 │
        │ 12  │ 3    │ Сумма двух значений.  │ 15      │ 01.02.2023 │ 09:14:20 │
        │ 12  │ 3    │ Сумма двух значений.  │ 15      │ 01.02.2023 │ 09:14:57 │
        └─────┴──────┴───────────────────────┴─────────┴────────────┴──────────┘

        Параметры:
        -------------
        отсутствует

    """

    # Класс --Table-- отвечает за красивый вывод информации в консоль.
    # Создать объект класса --Table--.
    table = Table(
        title="Недавние решённые задачи.",
        title_justify="center",
        title_style="bold red",
    )

    # Создание заголовок таблицы.
    table.add_column("X", style="blue")
    table.add_column("Y", style="blue")
    table.add_column("Операция", style="yellow")
    table.add_column("Решения", style="green")
    table.add_column("Дата", style="cyan")
    table.add_column("Время", style="cyan")

    # Извлечь все данные из таблицы [--history_decisions--].
    for value_1, value_2, operation, decision, date, time in cursor.execute(
        """SELECT * FROM history_decisions"""
    ):
        # Извлечёные данные добавляются в строки таблицы [-- table --].
        table.add_row(str(value_1), str(value_2), operation, str(decision), date, time)

    console = Console()
    console.print(table)


@decorate_func
def clean_history():
    """
    * Функция отвечает за очищение недавние задачи из файла recently_operations.db(База данных).

    Аргументы:
    -----------
    отсутствует

    """

    cursor.execute("DELETE FROM history_decisions")
    connection.commit()
