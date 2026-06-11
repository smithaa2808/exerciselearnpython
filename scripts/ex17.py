from sys import argv # import the 'argv' lists from the sys module to read the command line
from os.path import exists # import the 'exists' function to check if a file exists 

script, from_file, to_file = argv # assiging ex17.py, outfile.txt and languages.txt s argv , these words are came from the command given in the terminal 
# Accept the variable name and to know which script is being run
print(f"Copying from {from_file} to {to_file}") # informing the user that the contents are copied from from_file to to_file
# we could do these two on one line, how?
in_file = open(from_file) # opening the source file and assigned to in_file so we canread it 
indata = in_file.read() # reading the entire file and store it in indata 

print(f"The input file is {len(indata)} bytes long") #  informa the user how big the input file is 

# we could do these two on one line, how?
in_file = open(from_file) # opening the source file and assigned to in_file so we can read it 
indata = in_file.read() # reading the entire file and store it in indata
 
print(f"The input file is {len(indata)} bytes long") # informa the user how big the input file is 

print(f"Does the output file exist? {exists(to_file)}.") # asks the user wheather the file exist or not
print("Ready, hit RETURN to continue, CTRL-C to abort.") #  informing the user how to cancel or continue the programme 
input() # this pauses the programme and waits for the user to continue 

out_file = open(to_file,'w') # opening the file  and assigned to out_file so we can write it 
out_file.write(indata) # write the contents from input file to output file

print("Alright, all done.") # printing the strings

out_file.close() # informs the user that it is closing the file
in_file.close() # informs the user that it is closing the file 

