# Store student names and marks in a dictionary and print the average.
# Write to a text file the names of your 5 friends.
# Read the file and print each name.
# Count how many lines are in the file.
# Create a small contact book using a dictionary (name → phone number) and allow search.

students = {"A":"99", "B":"90", "C":"93"}

a = int(students["A"])
b = int(students["B"])
c = int(students["C"])

#print(len(students))
sum = a + b + c
average =  sum / len(students)
#print(average)

txt_file = open("challenge11_08_3.txt","w")


# frnd1 = input("Enter your friend name: ")
# frnd2 = input("Enter your friend name: ")
# frnd3 = input("Enter your friend name: ")
# frnd4 = input("Enter your friend name: ")
# frnd5 = input("Enter your friend name: ")

# txt_file.write(frnd1)
# txt_file.write("\n")
# txt_file.write(frnd2)
# txt_file.write("\n")
# txt_file.write(frnd3)
# txt_file.write("\n")
# txt_file.write(frnd4)
# txt_file.write("\n")
# txt_file.write(frnd5)


#txt_file.close()





contact_book = {
    "P1":"8994455440",
    "P2":"8994455540",
    "P3":"8094455440"
}
person_name = input("Give the person name")
# it should search for the number 
print(contact_book[person_name])

