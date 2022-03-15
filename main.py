# UML схема - https://drive.google.com/file/d/1ussGiYgc7ZGx1_4iUDrzSH1lP94k6a1O/view?usp=sharing

# При запуске программы сразу вылетела ошибка
#
# cannot import name 'User' from partially initialized module 'SiteUsers'
# (most likely due to a circular import)


from SiteUsers import *
from OrderEnvironment import *
from ItemsEnvironment import *
from CatalogEnvironment import *

# По-моему что не есть хорошая практика импортировать напрямую названиями классов

# создаем товары
item_1 = Item("Ritmix RWM-220", "Микрофон", 1000)
item_2 = Item("JBL T110", "Наушники-вкладыши с микрофоном", 1100)
item_3 = Item("Rombica Type-C Hub", "USB-разветвитель", 700)
item_4 = Item("Defender Next HB-440", "Клавиатура проводная", 500)
items = [item_1, item_2, item_3, item_4]

# инициализация каталога и подкаталогов
catalog_main = Catalog("Основной каталог")
subcatalog_1 = Catalog("Аудио товары")
subcatalog_2 = Catalog("Переферия для компьютера и ноутбука")

# формирование списков товара
item_list_catalog_1 = ItemList()
item_list_catalog_1.add_list_of_item(items[0:2], subcatalog_1)
item_list_catalog_2 = ItemList()
item_list_catalog_2.add_list_of_item(items[2:4], subcatalog_2)

# формирование каталогов
subcatalog_1.item_list = item_list_catalog_1
subcatalog_2.item_list = item_list_catalog_2
catalog_main.catalog_list = subcatalog_1
catalog_main.add_subcatalog(subcatalog_2)

# инициализация пользователей
user_1 = User("Игорь", "Матвеев")
admin_1 = Administrator("Админ", "Админов")

# формирование заказа пользователя
item_list_user_1 = ItemList()

# выбираем товары на покупку ( пока что в таком нечитаемом виде :( )
# (выбирается товар и ему соответствующие каталог, в котором лежит товар)
item_to_buy_1 = catalog_main.catalog_list[0].item_list.items[0][0]
item_to_buy_1_catalog = catalog_main.catalog_list[0].item_list.items[0][1]

item_to_buy_2 = catalog_main.catalog_list[1].item_list.items[0][0]
item_to_buy_2_catalog = catalog_main.catalog_list[1].item_list.items[0][1]

# добавляем выбранные товары в ItemList
item_list_user_1.add_item(item_to_buy_1, item_to_buy_1_catalog)
item_list_user_1.add_item(item_to_buy_2, item_to_buy_2_catalog)

# формируем детали заказа
order_user_1 = Order(user_1)
order_details_1 = OrderDetails(order_user_1, item_list_user_1)


# Для проверки, на подумать:
# catalog_main.catalog_list[0].item_list.items[0][0] - нормальный человек поймёт?











