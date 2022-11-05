# Python is an object oriented language. A Class is like an object constructor, or a blueprint for creating objects

class Car:
    def __init__(self, make, model, year, color):  # all classes have __init__ function which is executed when class
        self.make = make   # instance variable     # is initiated. It is assigning values to object properties
        self.model = model   # instance variable
        self.year = year   # instance variable
        self.color = color   # instance variable

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")

    wheels = 4   # class variable


car_1 = Car("Ford", "Mustang", 2017, "black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("-=-=-=-=-=-=-=-=-=-=-=-")
print(car_1.wheels)
print()
car_1.drive()
car_1.stop()

# inheritance - allows us to define a class that inherits all the methods and properties from another class
# parent class - is the class being inherited from, also called base class
# child class - is the class that inherits from another class, also called derived class


class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

    def eat(self):   # this is called method overriding, and it overwrites function to make it only for specific child
        print("This rabbit is eating")


class Fish(Animal):
    def swim(self):
        print("This rabbit can swim")


class Cat(Animal):
    def climb(self):
        print("This cat can climb")


rabbit = Rabbit()
fish = Fish()
cat = Cat()

print("-=-=-=-=-=-=-=-=-=-=-=-")
print(rabbit.alive)
rabbit.run()
rabbit.eat()
fish.sleep()
fish.swim()
cat.eat()
cat.climb()

# multi-level inheritance - when child class have another child class


class Country:
    borders = True


class State(Country):
    def states(self):
        print("This country have states")


class County(State):
    def county(self):
        print("This state have counties")


class City(County):
    def city(self):
        print("This county have cities")


city = City()
print("-=-=-=-=-=-=-=-=-=-=-=-")
print(city.borders)
city.states()
city.county()
city.city()

# multiple inheritance - when a child class is derived from more than one parent class


class Shape:
    def shape(self):
        print("Shape is a geometric figure")


class Rectangle:   # I can't contain rectangle as shape, because it will show TypeError
    def rectangle(self):
        print("Rectangle is a shape")


class Square(Shape, Rectangle):
    def square(self):
        print("Square is a shape and also rectangle (but rectangle isn't a shape)")


rectangle = Rectangle()
square = Square()

print("-=-=-=-=-=-=-=-=-=-=-=-")
square.shape()
square.rectangle()
square.square()


# method chaining - calling multiple methods sequentially. Each call performs an action on the same object and returns


class PC:
    def turn_on(self):
        print("You start the computer")
        return self   # this line is needed because it must be returned, otherwise python will return none

    def programming(self):
        print("You are programming on that computer")
        return self

    def play_games(self):
        print("You play games on computer")
        return self

    def turn_off(self):
        print("You turn off computer")
        return self


pc = PC()

print("-=-=-=-=-=-=-=-=-=-=-=-")
pc.turn_on().play_games().programming().turn_off()

# super function - function used to the methods of a parent class returns a temporary object of a parent class when used


class Shape1:
    def __init__(self, length, height):
        self.length = length
        self.height = height


class Triangle(Shape1):
    def __init__(self, length, height):
        super().__init__(length, height)   # Same arguments are contained in parent class to optimize the code

    def area(self):
        return (self.length*self.height)/2


class Pyramid(Shape1):
    def __init__(self, length, height, width):
        super().__init__(length, height)
        self.width = width

    def volume(self):
        return (self.length*self.width*self.height)/3


triangle = Triangle(5, 5)
pyramid = Pyramid(5, 5, 5)

print("-=-=-=-=-=-=-=-=-=-=-=-")
print(triangle.area())
print(pyramid.volume())

# abstract class - a class which contains one or more abstract methods
# abstract method - a method that has a declaration but does not have an implementation
# prevents a user from creating an object of that class and compels a user to override abstract methods in a child class
# child classes must implement all abstract methods in parent class

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


class Automobile(Vehicle):

    def go(self):
        print("You drive the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle")


# vehicle = Vehicle()
automobile = Automobile()
motorcycle = Motorcycle()

print("-=-=-=-=-=-=-=-=-=-=-=-")
# vehicle.go()
automobile.go()
motorcycle.go()

# duck typing - concept where the class of an object is less important than the methods/attributes. class type is not
#               checked if minimum methods/attributes are present. "if it walks like a duck, and it quacks like a duck,
#               then it must be a duck"


class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

print("-=-=-=-=-=-=-=-=-=-=-=-")
person.catch(duck)
print()
person.catch(chicken)

# passing objects as arguments


class Phone:

    color = None


def change_color(phone, color):

    phone.color = color


phone_1 = Phone()

print("-=-=-=-=-=-=-=-=-=-=-=-")
change_color(phone_1, input("Select your phone color: "))

print(phone_1.color, end=" ")
