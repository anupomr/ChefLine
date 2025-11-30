from app import validate_user, app
from custom_order import CustomOrder
from repository import RedisUserRepository
from user import PersonFactory

repo = RedisUserRepository()
factory = PersonFactory()
if __name__ == "__main__":
    print("\n🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️")
    print("\n🍴 ChefLine 🍴  Customer #1 Choice ❤️❤️")
    print("\n🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️")

    print("\n1. Login ")
    print("\n2. Signup ")
    print("\n3. Exit ")
    selection = int(input("\nEnter the number : "))

    if selection == 1:
        print("\nEnter Login ")
        user_name = input("\nEnter user_name : ")
        password = input("\nEnter password : ")
        if validate_user(user_name, password):
            app(user_name)
        else:
            print("Please check your username & Password")

    elif selection == 2:
        print("\nEnter Signup ")
        role = input("\nEnter your role : ")
        user_name = input("\nEnter user_name : ")
        password = input("\nEnter password : ")
        address = input("\nEnter your Address : ")
        user = factory.create_person(role, user_name, password, address)
        repo.save(user)
        print(user.user_name)

    elif selection == 3:
        exit(0)

    else:
        print("\nPlease Enter 1, 2 or 3 ")

    '''
        order = CustomOrder.customer_choice()
    print(f"\n✅ Final choice: {order}")
    '''
