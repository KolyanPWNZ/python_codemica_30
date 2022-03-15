# from OrderEnvironment import *

# Зацикленный импорт в модулях SiteUsers и OrderEnvironment
# - нужно что-то с этим делать
#
# Решил проблему тем что закомментировал импорт в данном модуле и
# в конце этого файла метод отмены заказа

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
    # def cancel_order(self, order):
    #     assert (type(order) == Order), "Некорректный тип заказа"
    #     order.status = 4





