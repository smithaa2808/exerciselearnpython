from sys import argv 
print(argv)
# read the WYSS section for how to run this
script, first, second, third = argv # assigning ex13.py A B C ,  these words came from commond given in the terminal

print("This script is called:", script) # printing the strings and ex13.py to know the readers that script  = ex13.py
print("Your first vriable is:", first) #  printing the strings and A 
print("Your second variable is:", second) #  printing the strings and B
print("You third variable is:", third) #  printing the strings nd C 

from sys import argv
script, user_name, my_name, your_name = argv

print("You are reading script:", script)
print("your first variable is:",  user_name)
print("your second variable:", my_name)


