# Parent class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

# Inherited method
dog.eat()

# Child class method
dog.bark()