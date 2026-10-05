# PythonOOP

#1 Classes and Objects
class SuperHero:
    def __init__(self,name:str,power:str,health:int,speed:int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

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





    