"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 1
Student Name: Judah Alter
Student ID: JAA22H
Section: 
Submission Date: [MM-DD-YYYY]
"""

# Problem 1 Planetary Cargo Weight Checker

planet = input("Enter the name of your planet where cargo is being shipped:(Earth, Mars, Moon)").lower()
items = int(input("Enter the number of items being shipped:"))

shippedtoEarth = 0
shippedtoMars = 0  
shippedtoMoon = 0

for n in range(items):
    weight = float(input("Enter the weight of item in kgs:"))
    if weight <=0:
        print("Invalid weight. Please enter a positive number.")
        continue
    if planet == "earth":
        shippedtoEarth += weight
        print(f"Total weight is {shippedtoEarth} kgs and is ok for the limit for Earth.")
        if shippedtoEarth > 500:
            print(f"Warning: Total cargo of {shippedtoEarth} kgs is too heavy for Earth.")
    elif planet == "mars":
        shippedtoMars += weight
        print(f"Total weight is {shippedtoMars} kgs and is ok for the limit for Mars.")
        if shippedtoMars > 300:
            print(f"Warning: Total cargo of {shippedtoMars} kgs is over the limit for Mars.")
    elif planet == "moon":
        shippedtoMoon += weight
        print(f"Total weight is {shippedtoMoon} kgs and is ok for the limit for the Moon.")
        if shippedtoMoon > 100:
            print(f"Warning: Total cargo of {shippedtoMoon} kgs is over the limit for the Moon.")
    else:
        print("Invalid planet name. Please enter Earth, Mars, or Moon.")
        break

    
# Problem 2 Astronaut Training Fatigue Tracker

Day = int(input("Enter the number of training hours tracked in a day:"))

for n in range(Day):
    fatigue = int(input("Enter your fatige level for the hour (0-10):"))
    


