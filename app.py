from custom_order import CustomOrder
from notifier import CookObserver, OrderSystem
from repository import RedisUserRepository
from user import PersonFactory

repo = RedisUserRepository()
factory = PersonFactory()


def validate_user(user_name, password):
    passcode = repo.get_password(user_name)
    if password == passcode:
        return True
    else:
        return False


def notify_all_cook():
    pass


def app(user_name):
    if repo.get_role(user_name) == "Customer":
        while True:
            print("\n ===== CUSTOMER VIEW ======")
            print("1. See Popular Menu and Order")
            print("2. Crate a custom Order ")
            print("3. Give a review")
            print("0. Logged Out")
            selection = input(" Select a number : ")
            if selection == "1":
                menus = repo.get_all_menus()
                print("\nPopular Menus:")
                for m in menus:
                    print(" -", m)
                item = input("Enter menu item to order: ")
                order = f"{user_name} ordered {item}"
                repo.save_order(order)
                print("Order placed successfully!")

            elif selection == "2":
                item = CustomOrder.customer_choice()
                print(f"\n✅ Final choice: {item}")
                order = f"{user_name} ordered {item}"
                repo.save_order(order)
                print("Order placed successfully!")
                chef1 = factory.create_person("cook", "anna@gmail.com", "pw223", "24 wed ave")
                chef2 = factory.create_person("cook", "anna2@gmail.com", "pw693", "44 wed ave")
                repo.save(chef1)
                repo.save(chef2)
                os = OrderSystem()
                os.register(CookObserver(chef1))
                os.register(CookObserver(chef2))
                os.create_msg(user_name, item)

            elif selection == "3":
                review = input("Write your review: ")
                full_review = f"{user_name}: {review}"
                repo.save_review(full_review)
                print("Review submitted!")

            elif selection == "0":
                print("Logged Out")
                break
            else:
                print("Invalid Selection")

    elif repo.get_role(user_name) == "Cook":
        while True:
            print("\n ===== COOK VIEW ======")
            print("1. Create and publish a menu")
            print("2. See Customer review")
            print("0. Logged Out")
            selection = input(" Select a number : ")
            if selection == "1":
                item_name = input("\n Enter a new menu Item : ")
                repo.save_menu(user_name, item_name)
                print(f"Menu Item {item_name} published ! ")

            elif selection == "2":
                reviews = repo.get_reviews()
                print("\nCustomer Reviews:")
                for r in reviews:
                    print(" -", r)

            elif selection == "0":
                print("Logged Out")
                break
            else:
                print("Invalid Selection : ")
    else:
        print("\n ===== ADMIN VIEW ======")
