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