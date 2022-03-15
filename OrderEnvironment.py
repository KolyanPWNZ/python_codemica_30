from SiteUsers import User
from CatalogEnvironment import *

# Зацикленный импорт SiteUsers

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
        # Почему нельзя словарь из статического поля присвоить именно полю status
        # - тогда и property задавать не нужно будет, и не нужно будет его валидировать
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
        self.__status = Order.__status_dict[status]

    # Насколько правильно применять ключевое слово assert в setter'ах?
    #
    # Из 2 минут гуглинга я выяснил что оно применятся для отладки программ (Debug),
    # не для того чтобы проверять и выкидывать AssertionError при валидации поля
    #
    # Для проверки типа под setter'ами думаю можно спокойно применять нормальную
    # встроенную функцию isinstance()
    #
    # Кажется assert впихивать везде не стоит, думаю вам нужно с этим подразобраться

    @property
    def id(self):
        return self.__id

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        assert (type(user) == User), "Объект не относится к классу User!"
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







