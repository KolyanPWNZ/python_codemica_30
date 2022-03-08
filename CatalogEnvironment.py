from ItemsEnvironment import Item


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

    # добавление товара (товару соответствует каталог, в котором он лежит)
    def add_item(self, item, catalog):
        # проверка входных данных:
        if type(item) != Item:
            assert "Некорректный тип товара"
        if type(catalog) != Catalog:
            assert "Некорректный id каталога"

        # добавление товара в список
        self.__items.append([item, Catalog])


class Catalog:
    __id = 0  # static field

    def __init__(self, item_list):
        self.__id = Catalog.__id
        Catalog.__id += 1
        self.item_list = item_list
        self.catalog = None

    # -----------------------------------------------------------
    @property
    def id(self):
        return self.__id

    @property
    def catalog(self):
        return self.__catalog

    @catalog.setter
    def catalog(self, catalog):
        if catalog is None or type(catalog) == Catalog:
            self.__catalog = catalog

    @property
    def item_list(self):
        return self.__item_list

    @item_list.setter
    def item_list(self, item_list):
        if type(item_list) == ItemList:
            self.__item_list = item_list
        else:
            assert "Список товаров должен относится к классу ItemList"
    # -----------------------------------------------------------

    # добавление подкаталога
    def add_subcatalog(self, item_list):
        self.catalog = Catalog(item_list)





