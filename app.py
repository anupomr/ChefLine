from repository import RedisUserRepository

repo = RedisUserRepository()
COOK_MENU = []


def validation(user_name, password):
    role = repo.get_role(user_name)
    print(role)
    passcode = repo.get_password(user_name)
    print(passcode)
    if role == "Customer" and password == passcode:
        return True
    else:
        return False


def create_menu():
    item_name = input("\n Enter a new menu Item : ")
    COOK_MENU.append({"name": item_name, "likes": 0})
    print(f"Menu Item {item_name} published ! ")
