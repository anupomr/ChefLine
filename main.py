# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def person_activity(self):
        pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
