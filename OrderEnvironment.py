from SiteUsers import User
from ItemsEnvironment import ItemList

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
        if type(user) == User:
            self.__user = user
        else:
            assert "Объект не относится к классу User!"
    # -----------------------------------------------------------


class OrderDetails:
    __id = 0 # static field

    def __init__(self, order, item_list):
        self.order = order
        self.item_list = item_list
        self.__id = User.__id
        User.__id += 1

    # -----------------------------------------------------------
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        if type(order) == Order:
            self.__order = order
        else:
            assert "Объект должен относится к классу Order"

    @property
    def item_list(self):
        return self.__item_list

    @item_list.setter
    def item_list(self, item_list):
        if type(item_list) == ItemList:
            self.__item_list = item_list
        else:
            assert "Объект должен относится к классу ItemList"
    # -----------------------------------------------------------







