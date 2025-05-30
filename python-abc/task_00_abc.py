#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())
