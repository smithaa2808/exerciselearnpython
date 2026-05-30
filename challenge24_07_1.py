# Write a function get_grade(score) that returns:

 #   "A" for 90+

  #  "B" for 80–89

   # "C" for 70–79

    #"F" for anything below 70

#def get_grade():  # defining the function get_grade without argument
   # print("The exam results are out. How much did you score?") # printing the statement 

    #score = int(input()) # asking the user to enter the marks

    #if 90 <= score <= 100: # condition
     #   print("Grade: A")  # prints the statement
    #elif 80 <= score <= 89:# condition
    #    print("Grade: B") # prints the statement
    #elif 70 <= score <= 80: #condition
     #   print("Grade: C") # prints the statement
    #else: 
     #   print("Grade: F")   # prints th estatement

#get_grade() # calling the function

def get_grade(score): # defining the function 

    if 90 <= score <= 100:  # condition
        print("Grade: A") # prints the statement
    elif 80<= score <= 89: # condition
        print("Grade: B")# prints the statement
    elif 70<= score <= 80: # condition
        print("Grade: C")# prints the statement
    else :
        print("Grade: F")# prints the statement
print(__name__) # it shows main or script name based on how the script is excuted 
# you can run the script either by calling the script in the terminal or by importing it in other file 
if __name__ == "__main__":
   print("The exam results are out. How much did you score?") #printing the statements 
   score = int(input()) # asking the user to enter marks
   get_grade(score)# calling the function
    
