"""
CIS-4930 Introduction to Python, Spring 2026
Homework : 1
Student Name: Judah Alter
Student ID: JAA22H
Section:3 
Submission Date: [01-22-2026]
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

hours = int(input("Enter the number of training hours tracked in a day: "))

maxFatigue = -1
DangerHours = 0
increase = 0
previous = None

for n in range(hours):
    fatigue = int(input(f"Enter your fatigue level for hour {n + 1} (0-10): "))

    if fatigue > maxFatigue:
        maxFatigue = fatigue

    if fatigue > 8:
        DangerHours += 1

    if previous is not None and fatigue > previous:
        increase += 1

    previous = fatigue

if DangerHours > 8:
    classification = "HIGH RISK - Medical review required"
elif increase > 3:
    classification = "MODERATE RISK - Extra rest recommended"
else:
    classification = "NORMAL - Proceed"

print(f"Hours tracked: {hours}, Max fatigue: {maxFatigue}, Dangerous hours: {DangerHours}, Increases: {increase}")
print(f"Training day classification: {classification}")


# Problem 3 Interactive Dungeon Door Code Puzzle


energy = 0

while True:
    energyEnter = float(input("Enter energy to add to the door (negative to remove):"))
    energy += energyEnter   

    exit = input("Write quit if you want to exit(anything else to continue):").lower()
    if exit == "quit":
        print()
        break
    if energy > 50:
        print(f"Door opens with energy {energy}")
        break
    elif energy < 0:
        energy = 0
        print("Door resets to 0.")
    else:
        print("Keep trying to open the door.")



# Problem 4 Librarian's Overdue Book Fine Calculator

BookType = input("Enter the type of book (novel, textbook, childrens):").lower()
DaysOverdue = int(input("Enter the number of days the book is overdue:"))
BorrowersAge = int(input("Enter the age of the borrower:"))

InitialFine = 0
TotalFine = 0
DiscountAmount = 0
OverdueFee = 0

if BookType not in ["novel", "textbook", "childrens"]:
    print("Invalid book type using novel pricing.")
    BookType = "novel"

if BookType == "novel":
    OverdueFee = 5
    InitialFine += DaysOverdue * 0.25
    TotalFine = InitialFine
    if BorrowersAge < 12:
        DiscountAmount = InitialFine * 0.50
        TotalFine = InitialFine - DiscountAmount
    elif InitialFine < 0:
        InitialFine = 0
        print("Total fine set to 0 since it was negative.")
    elif DaysOverdue > 30:
        TotalFine += OverdueFee
print(f"Books {BookType} overdue {DaysOverdue}, Borrower age {BorrowersAge}")
print(f"Base fine: ${InitialFine}")
print(f"Youth discount applied: -${DiscountAmount}")
print(f"Long overdue fee applied: +${OverdueFee if DaysOverdue > 30 else 0}")
print(f"Total due: ${TotalFine}")

if BookType == "textbook":
    OverdueFee = 5
    InitialFine += DaysOverdue * 0.5
    TotalFine = InitialFine
    if BorrowersAge < 12:
        DiscountAmount = InitialFine * 0.50
        TotalFine = InitialFine - DiscountAmount
    elif InitialFine < 0:
            InitialFine = 0
            print("Total fine set to 0 since it was negative.")
    elif DaysOverdue > 30:
            TotalFine += OverdueFee
print(f"Books {BookType} overdue {DaysOverdue}, Borrower age {BorrowersAge}")
print(f"Base fine: ${InitialFine}")
print(f"Youth discount applied: -${DiscountAmount}")
print(f"Long overdue fee applied: +${OverdueFee if DaysOverdue > 30 else 0}")
print(f"Total due: ${TotalFine}")

if BookType == "childrens":
    OverdueFee = 5
    InitialFine += DaysOverdue * 0.125
    TotalFine = InitialFine
    if BorrowersAge < 12:
        DiscountAmount = InitialFine * 0.50
        TotalFine = InitialFine - DiscountAmount
    elif InitialFine < 0:
        InitialFine = 0
        print("Total fine set to 0 since it was negative.")
    elif DaysOverdue > 30:
        TotalFine += OverdueFee
    
print(f"Books {BookType} overdue {DaysOverdue}, Borrower age {BorrowersAge}")
print(f"Base fine: ${InitialFine}")
print(f"Youth discount applied: -${DiscountAmount}")
print(f"Long overdue fee applied: +${OverdueFee if DaysOverdue > 30 else 0}")
print(f"Total due: ${TotalFine}")
    


#Problem 5 Guess the number with Adaptive Hunts

secret = 72
NumberofGuesses = 0

while True:
    guess = int(input("Enter your guess: "))
    NumberofGuesses += 1
    difference = abs(secret - guess)

    if guess == secret:
        print(f"Congratulations! Secret number is {secret}. You guessed the secret {secret} number in {NumberofGuesses} guesses.")
        break
    elif difference <= 5:
        print(f"Very Close. {'Too High.' if secret < guess else 'Too Low.'}")
    elif difference <=15 and difference > 5:
        print(f"Warm. {'Too High.' if secret < guess else 'Too Low.'}")
    else:
        print(f"Cold. {'Too High.' if secret < guess else 'Too Low.'}")







