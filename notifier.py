from abc import ABC, abstractmethod


# Observer Pattern Implementation

class Observer(ABC):
    @abstractmethod
    def update(self, order_message):
        pass


class Subject(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class OrderSystem(Subject):

    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

    def create_msg(self, customer_name, item):
        message = f"New order from {customer_name} : {item}"
        self.notify(message)


class CookObserver(Observer):
    def __init__(self, cook):
        self.cook = cook

    def update(self, order_message):
        print(f"[Cook {self.cook.user_name}] received order notification: {order_message}")


