# классы пользователей сайта магазина

class User:
    __id = 0  # static field

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__id = User.__id
        User.__id += 1

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            assert "Имя должно быть строкой!"

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) == str:
            self.__surname = surname
        else:
            assert "Фамилия должна быть строкой!"



class Administrator(User):

    def __init__(self, name, surname):
        super.__init__(name, surname)
