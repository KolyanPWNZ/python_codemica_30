from SiteUsers import User, Administrator
from OrderEnvironment import Order, OrderDetails
from ItemsEnvironment import Item
from CatalogEnvironment import Catalog, ItemList



user_1 = User("Игорь", "Матвеев")
print(user_1.name, user_1.surname, user_1.id)

admin_1 = Administrator("Админ", "Админов")
print(admin_1.name, admin_1.surname, admin_1.id)

order_1 = Order(user_1)

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
item_list_1 = ItemList()
item_list_1.add_list_of_item(items[0:2], subcatalog_1)
item_list_2 = ItemList()
item_list_2.add_list_of_item(items[2:4], subcatalog_2)

# формирование каталогов
subcatalog_1.item_list = item_list_1
subcatalog_2.item_list = item_list_2
catalog_main.catalog_list = subcatalog_1
catalog_main.add_subcatalog(subcatalog_2)








