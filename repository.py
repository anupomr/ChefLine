import json

import redis
from abc import ABC, abstractmethod
from config import host, port, password
from user import Customer


# Repository pattern implementations
class UserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass


class RedisUserRepository(UserRepository):
    def __init__(self):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )

    def save(self, user):
        self.redis_client.hset(user.user_name, mapping={
                                            "Password": user.password,
                                            "Address": user.address,
                                            "Role": user.get_role()})


'''
print(" Customer data Entered into Database")
cust = Customer("anupom@abc.com", "phys67", "81 Bay St")
role = cust.get_role()
print(role)
r.hset(cust.user_name, mapping={
    "Password": cust.password,
    "Address": cust.address,
    "Role": cust.get_role()})
    '''
