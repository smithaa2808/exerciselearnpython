def add(a, b): # defines a function that returns the sum of two numbers
    print(f"ADDING {a} + {b}") # displays message to the user which two values are added 
    return a + b  # it stores the value of a+b

def subtract(a, b): # defines a function to subtract b from a 
    print(f"SUBTRACTING {a} - {b}") # shows what is being subtracted 
    return a - b # it stores the value of a-b

def multiply(a, b): # defines a function that returns the multiplication of two numbers
    print(f"MULTIPLYING {a} * {b}") # displays message to the user which two values are multiplied
    return a * b # it stores the value of a*b

def divide(a, b): # create a reusable function that divides one number by another and returns the result 
    print(f"DIVIDING {a} / {b}") # shows what is being divided
    return a / b # it stores the value of a/b 


print("Let's do some math with just functions!") # displays message to the user

age = add(30, 5) # calls the add function with 30 and 5 , stores the result in age
height = subtract(78, 4) # subtract 4 from 78 and stores the result in height
weight = multiply(90, 2) # multipled 90 and 2 and stores the result in weight 
iq = divide(100, 2) # dividing 100 and 2 and stores the result in iq

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") # displays multiple varible value in a single sentence using f-string format


#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.") # displaying message to the user 

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # 

print("That becomes: ", what,  " Can you do it by hand?") # displays message to the user 