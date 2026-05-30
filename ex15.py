from sys import argv 

script, filename = argv # assigning filename 
print(filename)

txt = open(filename) # opening the file

print(f"Here's your file {filename}:") # printing f"strings{variable}
print(txt.read()) # reading the file 

print("Type the filename again:") # printing the strings

file_again = input("> ") # assigning file_again as >
txt_again = open(file_again) # opening the file

print(txt_again.read()) # reading the file 