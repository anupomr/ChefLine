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

    def save_menu(self, cook_name, menu_item):
        self.redis_client.rpush(f"COOK_MENU:{cook_name}", menu_item)

    def get_menu(self, cook_name):
        return self.redis_client.lrange(f"COOK_MENU:{cook_name}", 0, -1)

    def get_all_menus(self):
        keys = self.redis_client.keys("COOK_MENU:*")
        result = []
        for key in keys:
            result.extend(self.redis_client.lrange(key, 0, -1))
        return result

    def save_order(self, order):
        self.redis_client.rpush("ORDERS", order)

    def get_orders(self):
        return self.redis_client.lrange("ORDERS", 0, -1)

    def save_review(self, review):
        self.redis_client.rpush("CUSTOMER_REVIEWS", review)

    def get_reviews(self):
        return self.redis_client.lrange("CUSTOMER_REVIEWS", 0, -1)



