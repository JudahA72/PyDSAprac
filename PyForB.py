from typing import List
from typing import Tuple
from typing import Set
from typing import Dict

# Basics of Python for Beginners Review / 2027 SWE Recruiting

# Can can change the value of variables at any time (dynamic typing)
# running the program in terminal using the command python3 PyForB.py which python3 is version and PyForB.py is the name of the file
# you can run parts of the code in terminal by using the command python3 -i PyForB.py which will run the code and then leave you in an interactive shell where you can run parts of the code
# you use the interactive shell by typing in the variables and functions you want to run and it will return the output of that code, ctrl z to exit

# 1 - Introduction
print("hello world") # Can print text to the console

x = 6 # can define variables and assign values to them
y = 7

z = x + y # can perform basic math operations with variables
print(z) # can print the result of operations

print(" They said, \"Hello World!\"") # can print text with quotes in it using backslash or single quotes

# Runtime error, is an error that occurs while the program is running, as opposed to a syntax error which occurs when the code is being parsed. ex: division by zero, file not found, etc.
# Logical error, is an error that occurs when the program ran sucessfully but the output is not what was expected. ex: using the wrong variable in a calculation.

# 2 - Variables
message = "Hello World!" # can define variables and assign values to them
print(message) # can print the value of variables
message2 = 'Hello world!' # can use single quotes to define strings as well

# Since python is dynamic you can use the same name for a variable and change its value to a different type or string and if using it in a function it will use the most recent value of the variable

msg1,msg2 = "hello","World" # Can define multiple variables in one line, parallel assignment
print(msg1,msg2) # Can print multiple variables in one line
msg1,msg2 = msg2,msg1 # Can swap the values of two variables in one line
print(msg1,msg2) # This prints world hello because it uses the most recent value of the variables even though they were swapped 

# variable types include int, float, str, bool list set dict etc. using print(type) can tell you what type the value is associated with the variable

# you can type cast a variable to a different type using the type name as a function
x = "5"
print(int(x)) # this will print 5 as an integer not a string

# A type error occurs when you try to perform an operation on a variable that is not compatiable with its type.
# Can also use None to define a var with no value

# 3 - Math Operations
    # Operations follow pemdas and can be used with variables and numbers, % gives the remainder of a divsion, // gives rounded down result of integer, ** exponet
x=5
y=2
z=x//y
print(z) # prints 2 because 5//2 is 2.5 and it rounds down to 2

    #Boolean operations like or/and/not used to compare
    # or operation returns true if either of the two values is true, and returns false if both are false
    # and operation returns true if both values are true, and returns false if either is false
    # not operations returns true if the opposite occurs, so if the value is true it returns false etc
a,b,c = False,False,True
print(not(a)) # returns True
print(not(a and b)) # returns True

# 4 - Functions

def demo(n:int)-> bool:# function decleration includes keyword def, function name(greet) paraentheses that can include internal variables and colon to delcare
    # You should usually create type hints in your parameters as to show what each arguement should be n should be an integer and the function will return a bool in the end
    print("Hello world!") # indent to begin and put code in. Function cannot be empty,basic print statement for now
    print(n)#function now prints n
    msg = print(f"The final number is {x}") # can use f string to pass in variables or in this case the parameter for the function
    msg1 = print("This is the number printed in a diff way",x) # A comma can be used in the print statement to convert it to a string
    msg3 = print("Another print way " + str(n)) # You can string concatenate by converting it to a string using str()
    return True if n > 5 else False # can also use a return statement which will gave a value to the function so it can be called later not just plain running it

x = 10

result = demo(10) # now when calling the function you call by its name and any parameters it has when defined
# function now has a return statement which means now you can call upon its value at any time by setting another variable equal to its function call aka result
print(demo(3)) # Can also see output of function by calling it in a print statement which is common for functions that return something 
print(result)
demo(20)
# Parameters let the user pass different values to the functions and get different results
# An argument is the data you pass into the functions parameters to call it

def add_one(x:int)-> int:# simple function to show scope
    x += 1
    print("Added one to the value of x: ",x)
    return x

y = 10 # Basically I created this variable to act as the argument for this function when calling
add_one(y) # Basic function call that adds 1 to y and then prints that statement in the function as output
print(add_one(y)) # This function prints not only the statement made in the function but also the actual value produced by the function
# the output for the above function is Added one to the value of x: 11 and 11.
# This is because it not only runs the function but prints the value the function returns 
print(y) # The value outside the function y which is used for the argument is actually never changed because its on a global scope not affected by an interior functions local changes


# Functions can also be given default values like:
def example(name="Judah", letter = "J")-> None:
    print(name+letter)

example() # You can call the function using no arguements meaning not calling any of the values and it will use default ones
example("Steve") # You can also call function with arguements ranging up to the number of parameters changing 1 or all of the parameters values from their default one
example(name = "Marina", letter = "Z") # can call the function by actually using the parameter name. despite scope since your calling the example function you can reference parameters

# 5 - Conditional Arguements

def comparisonarg(x:int, y:int) -> bool:# creating a function to show comparison operations
    z = x==y # can actually set a variable equal to an operation
    print(z) # can print the value that operation provides
    return z # function returns the boolean value of operation 

comparisonarg(7,6)# prints and returns false

def comparison2(y:int,z:int)-> bool:
    return x<=y

x,y= 6,7
print("is x less than or equal to y here: ", comparison2(x,y))# string concatenate with , then call the function with arguments and it returns a boolean value based off inputs


def minimum(a:int, b:int)->int: #functions can also use if elif else statements to define what it should return
    if a>b:
        return a
    elif b>a and b>0: #can use opeartors like and or not inside of else if statements for conditions
        return b
    else:
        return a or b #can have it return either since this case is really saying since they are equal return either a or b

print(minimum(25,20))
print(minimum(25,-25))
print(minimum(25,25))
print(minimum(20,25))


# Weird use case truthy and falsey using an if statement to evalue to True or False

def is_truthy(value)->str:
    if value:
        return("Truthy")
    else:
        return("Falsy")

print(0,"is",is_truthy(0)) #Remember can use f"..{}" strings or , or + to concatenate strings and can have function call within print statements to show what function returns
print(10,"is",is_truthy(10))


# 6 - Loops

i = 0
while i<4: #while loop is mainly used to specify input until somehting happens to break loop
    print(f"This should print 4 times and the time now is {i}") #begins with 0 and goes to 3. Index at 0, length is 4, can also increment by any amount +=10 instead
    i+=1


for i in range(4): # for loops similar to while will print numbers 0-4
    print(i)

# Structure- For(keyword) then variable name being incremented, then in(keyword), then specify sequence to iterate. range is whatever set to in beginning to length - 1

for i in range(5,9,2): # can pass up to three arguments into range function so it will print from the range 5-8 iterating by 2 at a time so only prints 5 and 7, can also range backwards
    print(i)

# Nested Loops with question suppose you wanted to print all possible paris from set 1,2,3 and order of the pairs matter
# so 1,1 , 1,2 , 1,3
#    2,1 , 2,2 , 2,3
#    3,1 , 3,2 , 3,3
# can be accomplished by placing a loop inside of another called nested looping

for i in range(1,4):
    for j in range(1,4):
        print(f"{i},{j}")# each value is a seperate argument for the print function 
# prints it down by going through first loop so 1 then iterating through second 3 times so 1,1 1,2 1,3
# then you loop back and now its 2,1 2,2 2,3 and then to 3 for the same thing. So really first loop runs 3 times while second loop runs 9 times since its nested or 3x3=9
# loops do not create their own scope so you have to use different variable names for the nested loop
# inner loop runs to completion before outer loop continues


# can also use control flow statements which are break, pass , and continue

# 7 - Strings

def stringlength(str1:str, str2:str,)-> str: # function to return string length, using len() function
    if len(str1) >= len(str2): # operator to see if string1 is longer than string2 return string1
        return str1

    return str2

print(stringlength("Judah","Luca + Steven")) # prints string with longest length or str2

name = 'Judah'
for i in name: # this runs a for loop that returns each letter in order, iterating over the string name
    print(i)

print(name[4])# indexed 0-4 so it prints h in Judah
print(len(name)) # prints the actual length of the variable starting at index 1

my_string = "Hello, World!"

length = len(my_string) # 13

for i in range(length):
    print(my_string[i])

# basic example of using range function to print out each letter at each index
# range returns a sequence of numbers and lets you use index of each number to print it(important when needing index)
# in keyword lets you loop over string without needing index

new_string = "Judah, Alter!"
start,end = 1,5
print(new_string[start:end])# slicing this extracts the substring from new_string and prints from index 1 to 5

def first_n_characters(s: str, n: int) -> str:
    return s[:n]
#important function to demonstrate how when needing the first characters of something you slice almost backwards because you want it to end at n characters
# the opposite is true so to get the last n characters 

def last_n_characters(s:str, n:int) -> str:
    start = len(s) - n # this is done to get to find the last n characters in a list length of list minus n characters
    return s[start:] # returning all characters beginning at the index value of start

# can reverse a string by using the step as a negative number
 # print(string[start:end:step])
 # strings are also immutable 

# 8 - Lists(Important)

my_list = [1,2,3] # collection of items stored in a specific order and mutuable
 # List can be accessed based off index and length
 # List can be used in conditional statements 
 # Lists can be iterated using for loops

for element in my_list: # used in instead of range(len(my_list)) since its more consicse
    print(element)
    # only really use range(len) if you need the index if not then the in operator works fine

print(sum(my_list)) # 3 different functions that can sum or find the min/max of a list
print(min(my_list))
print(max(my_list))

my_list.append(4) # can add to the end of the list using the method append
# did not create a new list, original list has been modified
my_list.pop()
# you can pop from any index by specifing it or popping from the last n indexes using a for loop

def pop_n_from_list(new_list:List[int],n:int) -> List[int]:
    for i in range(n): # range n generates a sequence of numbers from 0 to n-1 
        new_list.pop() # you dont use i here bc it will actually pop at each index in loop rather than just the last index in loop one at a time
    return new_list # the loop simply acts as a counter to pop n times

print(pop_n_from_list([1, 2, 3, 4, 5], 2))

# can use the .index(element) method to print the index of the first occurence of element in the list
# can slice lists the same way you do strings [start:end:step]
 # Tuples are similar to lists except they are immutable and meant to be used to store related non changing data

my_tuple = (1,2,3)

# 9 - Sets
# Unordered, unique elements, can be converted to a list if order is important
# created with curly {} braces

my_set = set()
my_set.add(1) # add statements can take exactly one arugment
my_set.add(2)
my_set.add(1)

print(my_set) # will return only 1,2 since it cannot contain duplicate elements

# can remove elements in a set using .remove() and will return keyvalue error if element not present

my_set.remove(1)
print(my_set) # now removed 1 from set
# easy way to remove duplicates from a list by converting into a set then back into a new list
# can also use the keyword in to check if an element is present in list, this is an o(1) ST operation
# the in funciton acts as a bool check and returns True or False, can use len on sets



# 10 - Dicts
# key value pairs, mapping a key to a value -> hashmap
my_dict = {"Alice": 25, "Bob": 30, "Charlie": 35}

my_dict = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

# so we can delcare it like that or create it from scratch by using {}
new_dict = {}
new_dict["Judah"] = 22 # add key value pairs using square brackets
new_dict["Luca"] = 25
new_dict["Noah"] = 27
# dict values can be overwritten through reassigning
# the values in a dict can be of any type including other data structures
# the keys within a dictionary must be unique but the values can be the same

Judah_dict = {"a": [1, 2, 3], "b": {4, 5, 6}, "c": {"x": 7, "y": 8, "z": 9}}
# can check using in function for an element, the keys are ordered by order of insertion

# looping is very similar to lists, you can either loop over the keys which lets you access the values in the keys
# can also use the items which is more consice letting you loop over each pair instead of just key, however it takes 2 inputs that you iterate over rather than 1
for key,value in Judah_dict.items():
    print(key,value)
# will print it line by line by pairing

# example for contains duplicate characters in a string on how to get amount of each character

def count_characters(word:str)-> Dict[str,int]: # function takes a string word and converts into a dict
    count = {} # set an empty dictionary to add to

    for char in word: # looping through each character
        if char not in count:# if key does not exist yet cannot add it to its value, can access the count if you have not inserted the character yet
            count[char] = 0 # if a character is not inserted yet just set its value to 0 to avoid key value error
        count[char]+=1 # if encountered increase its value by 1
    return count


print(count_characters("Hello"))

# can remove item from dictionary using .pop() function or del keyword
# can also use .values in list to get the values of the keys if needed in a for loop or converting to a list

























    
