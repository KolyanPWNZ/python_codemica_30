from OrderEnvironment import Order, OrderDetails

# assert обычно применяется для отладки, но не для взаимодействия с пользователем
# лучше продумать альтернативный вариант проверок и делать обработчики неверных данных
# например можно, в случпе неверных данных блокировать покупку товара, а в качестве значения
# поля ставить None - на начальном этапе, и/или не менять значение поля до получения корректных данных
# в случае неверных данных следует уведомлять пользователя

# классы пользователей сайта магазина
class User:
    __id = 0  # static field

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__id = User.__id
        User.__id += 1

    # -----------------------------------------------------------
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        assert type(name) == str, "Имя должно быть строкой!"
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        assert type(surname) == str, "Фамилия должна быть строкой!"
        self.__surname = surname

    # -----------------------------------------------------------


class Administrator(User):
    # Т.к. тут наследдование, то можно было и для User и для Administrator использовать
    # единый счетчик id. Сейчас у объектов класса Administrator в памяти будет 2 поля с id
    # также создание пользователей Administrator будут увеличивать счетчик User.__id (пример ниже)

    # Для решения проблем можно использовать единый счетчик от User и удалить строчки с 51 по 63.
    __id = 0  # static field

    def __init__(self, name, surname):
        super(Administrator, self).__init__(name, surname)
        self.__id = Administrator.__id
        Administrator.__id += 1

    # ----------------------------------------------------------
    @property
    def id(self):
        return self.__id
    # ----------------------------------------------------------

    # отмена заказа
    def cancel_order(self, order):
        assert type(order) == Order, "Некорректный тип заказа"
        order.status = 4

# Пример со счетчиками объектов
test0 = Administrator('Test0','Test0')
test1 = User('Test1','Test1')
test2 = Administrator('Test0','Test0')
test3 = User('Test1','Test1')

print(test0.id, test1.id, test2.id, test3.id)