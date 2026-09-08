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

# 5 - Conditional Arguements




















    
