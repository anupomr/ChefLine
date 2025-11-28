from repository import RedisUserRepository

repo = RedisUserRepository()


def validation(user_name, password):
    role = repo.get_role(user_name)
    print(role)
    passcode = repo.get_password(user_name)
    print(passcode)
    if role == "Customer" and password == passcode:
        print("Success !! ")
    else:
        print("\nPlease Enter valid info ")


class Application:
    pass


validation("ric@abc.com", "phys67")
