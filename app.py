from repository import RedisUserRepository

repo = RedisUserRepository()
COOK_MENU = []
MENU_ITEM = [
    {"name": "Chicken Biriyani", "likes": 66}
]


def validate_user(user_name, password):
    passcode = repo.get_password(user_name)
    if password == passcode:
        return True
    else:
        return False


def create_menu():
    item_name = input("\n Enter a new menu Item : ")
    COOK_MENU.append({"name": item_name, "likes": 0})
    print(f"Menu Item {item_name} published ! ")


def popular_menu():
    print("Popular Mane")


def app(user_name):
    if repo.get_role(user_name) == "Customer":
        while True:
            print("\n ===== CUSTOMER VIEW ======")
            print("0. Logged Out")
            selection = input(" Select a number")
            if selection == "1":
                popular_menu()
            elif selection == "0":
                print("Logged Out")
                break
            else:
                print("Invalid Selection")

    elif repo.get_role(user_name) == "Cook":
        while True:
            print("\n ===== COOK VIEW ======")
            print("1. Create and publish a menu")
            print("0. Logged Out")
            selection = input(" Select a number : ")
            if selection == "1":
                create_menu()
            elif selection == "0":
                print("Logged Out")
                break
            else:
                print("Invalid Selection : ")
    else:
        print("\n ===== ADMIN VIEW ======")
