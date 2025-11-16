from abc import ABC, abstractmethod
import redis
from custom_order import CustomOrder


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


'''

r = redis.Redis(
    host='redis-14057.c52.us-east-1-4.ec2.redns.redis-cloud.com',
    port=14057,
    password='87g6Iqv4U73wSpFVlaAak3acu92uaLp3',
    decode_responses=True
)
print(" Customer data Entered into Database")
cust = Customer("adric@abc.com", "phys67", "81 Bay St")
role = cust.get_role()
print(role)
r.hset(cust.user_name, mapping={
    "Password": cust.password,
    "Address": cust.address,
    "Role": cust.get_role()})

print(" Customer data Entered into Database")
cust = Customer("adric@abc.com", "phys67", "81 Bay St")
role = cust.get_role()

r.hset(cust.user_name, mapping={
    "Password": cust.password,
    "Address": cust.address,
    "Role": cust.get_role()})

'''

order = CustomOrder.customer_choice()
print(f"\n🍴 Final choice: ")
