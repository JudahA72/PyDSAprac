"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 1
Student Name: Judah Alter
Student ID: JAA22H
Section:3 
Submission Date: [02-05-2026]
"""

# Problem 1 Campus WIFI Access Log Analyzer

wifi_logs = [
("LIB", 45, 9), # building, devices, hour
("LIB", 92, 11),
("CSC", 67, 14),
("LIB", 78, 13),
("ENG", 120, 10),
("CSC", 55, 15),
("ENG", 89, 16)
]

mywifi_logs = [
("LIB", 54, 9), # building, devices, hour. Used this to check my code with different data
("LIB", 29, 11),
("CSC", 76, 14),
("LIB", 87, 13),
("ENG", 210, 10),
("CSC", 55, 15),
("ENG", 98, 16)
]


BusyBuildings = set()
for building, devices,hour in wifi_logs:
    if devices > 50:
        BusyBuildings.add(building)

PeakHour = [entry for entry in wifi_logs if entry[1] >= 80]

LibraryDevices = [devices for building,devices,hour in wifi_logs if building == "LIB"]
LibrarySlice = LibraryDevices[:]

count = {}
for building, devices, hour in wifi_logs:
    if building not in count:
        count[building] = [0,0] # this is for the current sum of devices and the current count of devices
    count[building][0] += devices
    count[building][1] += 1

BusyBuildings = None
BusyBuildingsAvg = 0.0
for building, (devices,count) in count.items():
    average = devices / count
    if average > BusyBuildingsAvg or BusyBuildings is None:
        BusyBuildingsAvg = average
        BusyBuildings = building

print(f"Busy Buildings(>50): {BusyBuildings}")
print(f"Peak Hour(>=80): {PeakHour}")
print(f"Library Devices: {LibrarySlice}")
print(f"Busiest: {BusyBuildings} (avg {BusyBuildingsAvg:.2f} devices.)")


# Problem 2 University Course Enrollment Analyzer

Courses = {
    "CIS-4930": {
        "title": "Introduction to Python",
        "credits": 3,
        "prereqs": ["COP-3014", "COP-3330"],
    },
    "COP-3014": {
        "title": "Programming I",
        "credits": 3,
        "prereqs": [],
    },
    "COP-3330": {
        "title": "Object-Oriented Programming",
        "credits": 3,
        "prereqs": ["COP-3014"],
    },
    "CIS-3250": {
        "title": "Ethics in Computer Science",
        "credits": 3,
        "prereqs": [],
    },
    "CDA-3100": {
        "title": "Computer Organization I",
        "credits": 3,
        "prereqs": ["COP-3014"],
    },
}

CodeTry= input("Enter the course code to look up (CIS-4930, COP-3014 etc.): ")

Code = "".join(CodeTry.split()).upper() # This is to remove any spaces and make it uppercase, since course codes are usually in uppercase and if the user puts a white space it can still read it. Join is very useful lol. 

if Code in Courses:
    course = Courses[Code]
    title = course["title"]
    credits = course["credits"]
    prereqs = course["prereqs"]
    print(f"{Code}: {title}({credits} credits)")
    print("Prerequisites: " + (", ".join(prereqs) if prereqs else "None")) # Googled join, since there can be more than one prereq.

    TotalCredits = credits
    for prereq in prereqs:
        if prereq in Courses:
            TotalCredits += Courses[prereq]["credits"]

    print(f"Total credits with prereqs: {TotalCredits}")
else:
    print(f"Course code {Code} not found.")



# Problem 3 Cafeteria Menu & Order Validator


LargerMenu = {
    "burger": {"price": 5.50, "category": "main"},
    "fries": {"price": 2.00, "category": "side"},
    "soda": {"price": 1.50, "category": "drink"},
    "salad": {"price": 4.25, "category": "side"},
    "coffee": {"price": 2.75, "category": "drink"},
}

print("Menu:")
for item, info, in LargerMenu.items():
    price = info["price"]
    category = info["category"]
    print(f"{item.title()} (${price:.2f}) - {category}")

order = []

try:
    OrderItems = int(input("How many different items do you want?"))
except ValueError: # value error comes in handy as it can prevent a crash and keep it going
    print("Invalid input for number of items. Need to enter an integer.")
    OrderItems = 0

for i in range(OrderItems):
    item = input(f"Enter item name {i + 1}:").lower()
    try:
        quantity = int(input(f"Enter quantity for {item}:"))
    except ValueError:
        quantity = 0
        print("Invalid input so setting to 0")
    
    order.append({"item": item, "quantity": quantity})
    
print("\nOrder:")
total = 0.0

for entry in order:
    item = entry["item"]
    quantity = entry["quantity"]

    if item in LargerMenu:
        price = LargerMenu[item]["price"]
        Totals = price * quantity
        total += Totals
        print(f"{item} x{quantity}@ ${price:.2f} = {Totals:.2f}") #used this to round up to 2 decimal places just in case there are some weird outputs
    else:
        print(f"'{item}' is not on the menu.")

print("--------------")
print(f"Total: ${total:.2f}")


# Problem 4 Configurable Data Processor

import data_utils

readings = [1.2, 1.8, 2.1, 10.0, 1.9, 2.0, 1.7]  # 10.0 is not > 3σ mathematically
cleaned = data_utils.process_sensor_data(
    readings,
    remove_outliers=True,
    smooth=True,
    scale="normalize",
)

print("Cleaned:", cleaned)


# Problem 5 Library Checkout System

import library

Inventory = [
    {"title":"Python Crash Course", "status": "available"},
    {"title":"Clean Code", "status": "checked_out", "due_date": "2026-02-01"},
    {"title":"Django for Beginners", "status": "available"},
    {"title":"Fluent Python", "status": "checked_out", "due_date": "2026-02-10"},
    {"title":"Automate the Boring Stuff", "status": "checked_out", "due_date": "2026-01-20"},
]

library.print_inventory(Inventory)

TotalBooks = len(Inventory)
AvailableBooks = sum(1 for Book in Inventory if Book["status"] == "available")

OverdueBooks = 0
for Book in Inventory:
    if Book["status"] == "checked_out" and "due_date" in Book:
        Days = library.days_overdue(Book["due_date"], library.TodayDate)
        if Days > 0:
            OverdueBooks += 1

print(f"Summary: {TotalBooks} books total, {AvailableBooks} available, {OverdueBooks} overdue")





