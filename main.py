from SiteUsers import User, Administrator

user_1 = User("Игорь", "Матвеев")
print(user_1.name, user_1.surname, user_1.id)

admin_1 = Administrator("Админ", "Админов")
print(admin_1.name, admin_1.surname, admin_1.id)

