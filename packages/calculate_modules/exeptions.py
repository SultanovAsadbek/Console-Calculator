class TypeExc(Exception):
    """
    Класс исключение --TypeException--
    Класс вызывается в случи если:
        * пользователи введут строку вместо цифры.
        * пользователи ничего не введут (пустая строка).

    Аттрибуты:
    -------------
    head : str
        заголовок.
    message : str
        сообщения об конкретном ошибке.

    """

    def __init__(self, head="ToDoTaskTypeError", message="Bad Type!"):
        super().__init__(message)
        self.head = head
        self.message = message
