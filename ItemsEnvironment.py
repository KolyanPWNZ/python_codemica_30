

class Item:
    __id = 0  # static field

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.__id = Item.__id
        Item.__id += 1

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

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if type(quantity) == int and quantity >= 0:
            self.__quantity = quantity
        else:
            assert "Количество товаров должно быть целым числом больше нуля"



class ItemList:
    __id = 0  # static field

    def __init__(self):
        self.__id = ItemList.__id
        ItemList.__id += 1
        self.__items = list() # список товаров и id каталогов, которым они соответствуют

    @property
    def id(self):
        return self.__id

    @property
    def items(self):
        return self.__items

    # добавление товара (товару соответствует id каталога, в котором он лежит)
    def add_item(self, item, catalog_id):
        # проверка входных данных:
        if type(item) != Item:
            assert "Некорректный тип товара"
        if catalog_id < 0:
            assert "Некорректный id каталога"

        # добавление товара в список
        self.__items.append([item, catalog_id])






