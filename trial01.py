input_file = "typing01.txt" # assinging inputfile
txt = open(input_file,"r") # opening file

output_data = txt.read() # reading the file 
print(output_data) # printing the data
get_words = output_data.split(" ") # spliting the data into words 
print(get_words) # printing the splitted words 
nwords = len(get_words) # count of list of words 
print(nwords) # count of words 
txt.close() # closing the file 