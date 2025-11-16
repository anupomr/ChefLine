from abc import ABC, abstractmethod


# Abstract class

class Person(ABC):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    @abstractmethod
    def get_role(self):
        pass


class Customer(Person):

    def __init__(self, user_name, password, address):
        super().__init__(user_name, password)
        self.address = address

    def get_role(self):
        return "Customer"


class Cook(Person):

    def __init__(self, user_name, password, address):
        super().__init__(user_name, password)
        self.address = address

    def get_role(self):
        return "Cook"


class Admin(Person):

    def __init__(self, user_name, password, address):
        super().__init__(user_name, password)
        self.address = address

    def get_role(self):
        return "Admin"


# Factory pattern implementation

class PersonFactory:

    @staticmethod
    def create_person(role, user_name, password, address):
        role = role.lower()

        if role == "customer":
            return Customer(user_name, password, address)

        elif role == "cook":
            return Cook(user_name, password, address)

        elif role == "admin":
            return Admin(user_name, password, address)

        else:
            raise ValueError(f"Unknown role type : {role}")
