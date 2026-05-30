print("Let's practice everything.") # displying message to the user 
print('You\'d need to know \'bout escapes with \\ that do:') # displaying message to the user 
print('\n newlines and \t tabs.') # displaying message to the user , \n takes to the next line, \t gives extra space 
# printing the strings
poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
an requires an explain 
\n\t\twhere there is none.
"""  # just as a command for upcoming lines

print("-------------")  # displaying message to the user 
print(poem) # displaying message to the user 
print("-------------") # displaying messsage to the user 

five = 10 - 2 + 3 - 6 # just as a command for upcoming lines 
print(f"This should be five: {five}") # displaying message to the user 

def secret_formula(started): # defining the function secret_formula and giving the varible started as input 
    jelly_beans = started * 500 # showa multiplication of base value 
    jars = jelly_beans / 1000 # divides the number of jelly_beans by 1000 and stores the end result in the variable jars 
    crates = jars / 100 # divides the number of jars by 100 and stores the end result in the variable jars
    return jelly_beans, jars, crates 


start_point = 10000 # just as a command for upcomig lines 
beans, jars, crates = secret_formula(start_point) # calls a function and unpackits multiple return value into three seperate values   

# remeber that this is another way to format a string
print("With a starting point of: {}".format(start_point)) # displayiing message to the user , the value of start_point is used in the place of {}
# it's just like with an f"" string 
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") # displaying message to the user

start_point = start_point / 10 # reduces the value of star_point by a factor of 10

