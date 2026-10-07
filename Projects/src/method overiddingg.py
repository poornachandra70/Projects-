# Parent class
class Animal:

    def sound(self):
        print("Animal makes sound")


# Child class
class Dog(Animal):

    # Overriding parent method
    def sound(self):
        print("Dog says: Bark")


dog = Dog()

dog.sound()