import json

import redis
from abc import ABC, abstractmethod
from config import host, port, password
from user import Customer, PersonFactory


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

    def delete(self, user_name):
        self.redis_client.delete(user_name)

    def get_password(self, user_name):
        result = self.redis_client.hget(user_name, "Password")
        return result

    def get_address(self, user_name):
        result = self.redis_client.hget(user_name, "Address")
        return result

    def get_role(self, user_name):
        result = self.redis_client.hget(user_name, "Role")
        return result
