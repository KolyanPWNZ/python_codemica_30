from SiteUsers import User, Administrator
from OrderEnvironment import Order, OrderDetails
from ItemsEnvironment import Item
from CatalogEnvironment import Catalog, ItemList

user_1 = User("Игорь", "Матвеев")
print(user_1.name, user_1.surname, user_1.id)

admin_1 = Administrator("Админ", "Админов")
print(admin_1.name, admin_1.surname, admin_1.id)

order_1 = Order(user_1)