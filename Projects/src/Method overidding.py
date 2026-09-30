class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts using a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts using a button")


car = Car()
bike = Bike()

car.start()
bike.start()