# Write a function that returns the square of a number.
# Reverse a string entered by the user.
# Count the vowels in a given string.
# Check if a word is a palindrome (same forwards and backwards).
# Create a function that converts Celsius to Fahrenheit.

#line1 = input("Enter a string: ")
#spliting = line1.split(' ')
#print(spliting)
#spliting.reverse()
#print(spliting)
#print(' '.join(spliting))

#temperature = int(input("Enter the temperature in celsius: "))
#fahrenheit = (temperature * 9 / 5) + 32
#print(fahrenheit)

#number = (input("Enter a number: "))

#def square_number(value):
    
#    if not number.isdigit():
#        print("Type a number ")

#    else:
#        result = int(number)
#        point = result * result
#        print(point)

#square_number(number)

#letter = ["d", "e", "e", "d"]
#joining = (''.join(letter))
#letter.reverse()
#joining_2 = (''.join(letter))
#print(joining)
#if joining == joining_2:
#    print("True")

#else:
#   print("False")

vow_count = 0
word = "greatidea"
for char in word:
    if char in ["a","e","i","o","u"]:
        vow_count += 1
print(vow_count)



