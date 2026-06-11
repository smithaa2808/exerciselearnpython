# this one is like your scripts with argv
def print_two(*args): # defines a function that can two or more arguments 
    arg1, arg2 = args # extract the individual value so they can be used inside the function
    print(f"arg1: {arg1}, arg2: {arg2}") # to display the values of arg1 and arg2

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # defines a function that have 2 arguments
    print(f"arg1: {arg1} arg2: {arg2}") # to display the values of arg1 and arg2

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # defines a function that have 2 arguments
    print(f"arg1: {arg1}, arg2: {arg2}") # to display the values of arg1 and arg2

# this one takes no arguments
def print_none(): # defines a function called print_none that does not take any argument
    print("I got nothin.") # displays message to the user

print_two("Zed","Shaw") # this line is given to pass the argumentsn to a function and show how they are printed using args 
print_two_again("Zed","Shaw")  # call the function that take twp arguments and prints directly
# print_none("First!") 
print_none() # call the function that take no arguments and prints a message
