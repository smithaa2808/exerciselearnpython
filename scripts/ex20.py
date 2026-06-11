from sys import argv # import the 'argv' lists from the sys module to read the command line 

script, input_file = argv # Accept the variable name and to know which script is being run 

def print_all(f): # this defining  a function named print_all and giving it the variable f as input
    print(f.read()) # reads the full content of the file and displays it to the reader  

def rewind(f): # defines the function to read the file again from start 
    f.seek(0) # moves the file to the start of the file

def print_a_line(line_count, f): # it creates afunction that prints asingle line from a file and shows the line number
    print(line_count, f.readline()) # this print the line number along with the next line from the file 

current_file = open(input_file) # opening the source file and assigned to current_file so we can read the file
print(current_file.read())
print("test")
current_file.seek(0)
print(current_file.readline())
#print("First let's print the whole file:\n") # displays message to the user and \n takes to the next line 

#print_all(current_file) # calls the print_all function to display the entire content of the current file

#print("Now let's rewind, kind of like a tape.") # displays message to the user 

#rewind(current_file) # allows to re read the file from the beginning 

#print("Let's print three lines:") # displaying the message to the user 

#current_line = 1  # tracks the current line number
#print_a_line(current_line, current_file) # to print the line number and the next line from the file 

#current_line = current_line + 1 # tracks the current line number
#print_a_line(current_line, current_file) # to print the line number and the next line from the file 

#current_line = current_line + 1 # tracks the current line number
#print_a_line(current_line, current_file) # to print the line number and the next line from the file 



