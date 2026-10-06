# PythonOOP

#1 Classes and Objects
class SuperHero:
    def __init__(self,name:str,power:str,health:int,speed:int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
        """A class to represent a superhero, this is called a doc string meant to describe the functions I create, instead of # comments."""


    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def take_damage(self,amount:int):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    # These functions declared inside of the class are called methods and can be called outside of the class using the.() opeartor

    # This is a class, defined by keyword class with a name SuperHero
    # it acts as a blueprint for objects
    # the init method is a special method that runs automatically, it sets the object's starting attributes
    # the self variable is what allows us to add objects to our attributes to our object
    # self represents the instance of a class, and when creating an object from a class it passes the object as the first argugement to the __init__ method(self is what is standardly used)


Hero= SuperHero("SpiderMan","Webs and Agility",20,30) # this is creating an object based off of the SuperHero class, parameter order must match the init method
print(f"{Hero.name} has a power of {Hero.power} with level {Hero.health} health and speed of level {Hero.speed}")

# Can also change values of parameter outside of function

Hero.power = "Spider Sense"
print(f"{Hero.name} has a power of {Hero.power} with level {Hero.health} health and speed of level {Hero.speed}")

Hero.health = 30
Hero.speed = 40 

print(f"{Hero.name} has a power of {Hero.power} with level {Hero.health} health and speed of level {Hero.speed}")
# these examples are meant to showcase the arguments in the object Hero are mutuable 

Hero.take_damage(12)
# This calls one of the methods take_damage inside the class SuperHero in which the hero takes damage, arguemt is provied at the call and that is what is passed in
# self is mandatory to be used in the parameters of all methods, it is a python convention and how each hero can have their own set of attributes/powers

# the __init__ method is used to initialize the attributes of the new object and when an object is being created the init method initalizes everything
# self is always the first parameter in method definitions


# 2- Encapsulation
# Encapsulation is the concept of wrapping data and methods that work on the data within one unit, called a class. In addition, it restricts access to some of the object's components.
# Main goal is to hide the internal details of an object and only expose what is neccessary
# You only need to know how to opearte the car, not how it works

# the attribues above for the SuperHero class are actually public attributes that is why they can be accessed outside of the class














    