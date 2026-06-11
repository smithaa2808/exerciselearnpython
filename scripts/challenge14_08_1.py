# Odd/Even & Divisible by 5
# Write a program that takes a number from the user and checks:
# If it’s odd or even
# If it’s also divisible by 5

#num = int(input("Enter a number: "))
#result = num % 2
#value = num % 5
#if result == 0  and value == 0:
#	print("TRUE")
#else:
#	print("FALSE")

# Grade Classification
# Take a student’s marks as input and print:
# "Fail" if less than 40
# "Pass" if 40–59
# "Merit" if 60–79
# "Distinction" if 80+

#marks = int(input("Enter your mark: "))

#if marks < 40:
#	print("FAIL")
#elif 40 <= marks <= 59:
#	print("PASS")
#elif 60 <= marks <= 79:
#	print("MERIT")
#else:
#	print("DISTINCTION")

# Leap Year Checker
# Given a year, check if it’s a leap year using the rule:
# Divisible by 4 and not divisible by 100
# OR divisible by 400

# year = int(input("Enter a year: "))
# check = year % 100
# if check != 0:
# 	print("It's a leap year")
# else:
# 	print("Just a normal year")


# Three Number Comparison
# Take 3 numbers from the user and print the largest one without using max().

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: ")) 
# values = []
# values.append(num1)
# values.append(num2)
# values.append(num3)

# total = 0
# highest = values[0]


# for greater in values:
# 	#print(greater)
# 	total += greater
# 	#print(total)
	
# if greater > highest:
# 	highest = greater
# 	print(highest)

# ans1 = int(input("Enter the first number:  "))
# ans2 = int(input("Enter the second number:  "))
# ans3 = int(input("Enter the third number:  "))

# list = []

# list.append(ans1)
# list.append(ans2)
# list.append(ans3)

# def largest():
#     total = 0
#     highest = list[0] 
#     for i in list:
#         total += highest
#     if i > highest:
#         highest = i
#         print(highest)
# largest()       

# Character Type Check
# Take a single character from the user and check if it’s:
# Uppercase letter
# Lowercase letter
# Digit
# Special character

def character(validating_character):
	
	if not validating_character.istitle():
		print("False")
	elif not validating_character.islower():
		print("False")
	elif not validating_character.isdigit():
		print("False")
	elif not validating_character.isascii():
		print("False")
	else:
		print("True")
if __name__ == "__main__":
	validating_character = input("Enter a character:  ")
	character(validating_character)



