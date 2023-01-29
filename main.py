# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod


class GreetingInterface(ABC):
    @abstractmethod
    def greeting(self) -> str:
        ...


class Hello(GreetingInterface):

    def greeting(self) -> str:
        return "Hello"


# todo: Welcome Class


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    greeting: GreetingInterface = Hello()
    print(greeting.greeting())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
