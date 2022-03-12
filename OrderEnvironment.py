from SiteUsers import User
from CatalogEnvironment import ItemList

class Order:
    __id = 0  # static field
    __status_dict = {
        0: "Заказ обрабатывается",
        1: "Заказ в пути",
        2: "Заказ прибыл",
        3: "Заказ завершен",
        4: "Заказ отменен"
    }

    def __init__(self, user):
        self.user = user
        self.__id = Order.__id
        Order.__id += 1
        self.status = 0 # статус заказа

    # -----------------------------------------------------------
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        # установка статуса заказа
        assert type(status) == int, "Статус должен быть целым числом"
        assert status in Order.__status_dict, "Такого статуса нет"

        # Тут лучше хранить число, меньше памяти будет занимать объект
        # А преобразование в строку делать при выводе статуса, т.е. геттер изменить так:
        # @property
        # def status(self):
        #    return Order.__status_dict[self.__status]
        self.__status = Order.__status_dict[status] # заменить на self.__status = status

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
