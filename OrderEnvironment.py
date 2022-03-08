from SiteUsers import User
from CatalogEnvironment import ItemList

class Order:
    __id = 0  # static field

    def __init__(self, user):
        self.user = user
        self.__id = Order.__id
        Order.__id += 1

    # -----------------------------------------------------------
    @property
    def id(self):
        return self.__id

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        assert type(user) == User, "Объект не относится к классу User!"
        self.__user = user

    # -----------------------------------------------------------


class OrderDetails:
    __id = 0 # static field

    def __init__(self, order, item_list):
        self.order = order
        self.item_list = item_list
        self.__id = OrderDetails.__id
        OrderDetails.__id += 1

    # -----------------------------------------------------------
    @property
    def id(self):
        return self.__id

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        assert type(order) == Order, "Объект должен относится к классу Order"
        self.__order = order

    @property
    def item_list(self):
        return self.__item_list

    @item_list.setter
    def item_list(self, item_list):
        assert type(item_list) == ItemList, "Объект должен относится к классу ItemList"
        self.__item_list = item_list

    # -----------------------------------------------------------







