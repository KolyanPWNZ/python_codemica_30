

class Item:
    __id = 0  # static field

    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price
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
        assert type(title) == str, "Название товара должно быть строкой"
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        assert type(description) == str, "Описание товара должно быть строкой"
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        # А как же копейки?))) Маркетинговых фишек не будет, например 99.99)))
        assert type(price) == int and price > 0, "Цена товара должна быть целым числом больше нуля"
        self.__price = price

    # -----------------------------------------------------------
