

class Item:
    __id = 0  # static field

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.__id = Item.__id
        Item.__id += 1

    # -----------------------------------------------------------
    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) == str:
            self.__title = title
        else:
            assert "Название товара должно быть строкой"

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if type(description) == str:
            self.__description = description
        else:
            assert "Описание товара должно быть строкой"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) == int and price > 0:
            self.__price = price
        else:
            assert "Цена товара должно быть целым числом больше нуля"
    # -----------------------------------------------------------








