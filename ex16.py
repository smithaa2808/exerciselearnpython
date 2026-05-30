filename = input("Give the file name ") # asking for filename for printing and opening 
print(f"We're going to erase {filename}.") # telling the user the contents in the file are going to earse
print("If youdon't want that, hit CTRL-C (^C).") # informing the user how to cancel the programme if they don't want to continue
print("If you do want that, hit RETURN.") # informing the user how to continue with the given command
# printing the strings
input("?") # asking the user to type something, it uses the text typed by the user alter in the programme

print("Opening the file...") # informing the user that it is about to open the file 
target = open(filename, 'w') # opening the filename for writing and saved the file as target 

print("Truncating the file. Goodbye!") # informing the user that the file is being earsed 
target.truncate() # earses apart of a file 

print("Now I'm going to ask you for three line.") # informing the user that the programme is going to ask three lines
line1 = input("line 1: ") # line1 is assigned as "line 1:" # asking the user to enter a line and store the input  
line2 = input("line 2: ") # line2 is assigned as "line 2:" # askking the user to enter a line and store the input
line3 = input("line 3: ") # line3 is assignes as "line 3:" # asking the user to enter a line and store the input 

print("I'm going to write these to the file.") # informing the user that those are going to printed in the file

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")       
target.write(line3) 
target.write("\n")



print("And finally, we close it.") # informs the user that the file is going to close 
target.close() # closes the file and saves all changes 


