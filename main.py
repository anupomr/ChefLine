
from custom_order import CustomOrder
from repository import RedisUserRepository
from user import PersonFactory

if __name__ == "__main__":
    print("\n🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️")
    print("\n🍴 ChefLine 🍴  Customer #1 Choice ❤️❤️")
    print("\n🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️🍽️")

    print("\nEnter Signup ")
    role = input("\nEnter your role : ")
    user_name = input("\nEnter user_name : ")
    password = input("\nEnter password : ")
    address = input("\nEnter your Address : ")
    factory = PersonFactory()
    user = factory.create_person(role, user_name, password, address)
    repo = RedisUserRepository()
    repo.save(user)
    print(user.user_name)

    '''
    
    order = CustomOrder.customer_choice()
    print(f"\n✅ Final choice: {order}")
    '''
