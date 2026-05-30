#Triangle Type
#Take the lengths of three sides of a triangle and check whether it is:
#Equilateral
#Isosceles
#Scalene
#Also check if the sides actually form a triangle. 

# side1 = int(input("Enter the length of side1: "))
# side2 = int(input("Enter the length of side2: "))
# side3 = int(input("Enter the lenght of side3: "))

# def triangle():
#     if side1 + side2 > side3 :
#         print("It forms a triangle")
#     elif side2 + side3 > side1:
#         print("It forms a triangle")
#     elif side1 + side3 > side2:
#         print("It forms a triangle")
#     else:
#         print("This is not a triangle")

# def type_triangle():
#     if side1 == side2 == side3:
#         print("This is an equilateral triangle")
#     elif side1 == side2 != side3:
#         print("This is an isocleles triangle")
#     elif side1 == side3 != side2:
#         print("This is an isocleles triangle")
#     elif side2 == side3 != side1:
#         print("This is an isocleles triangle")
#     else:
#         print("This is a scalene triangle")

# triangle()
# type_triangle()

    
#ATM Withdrawal Conditions
#Input withdrawal amount and account balance. Check if:
#Amount is a multiple of 100
#Amount ≤ balance
#If yes, print new balance, else print error.

# with_drawal_amount = int(input("Enter the amount to withdraw: "))
# account_balance = int(input("Enter the account balance: "))
# value = with_drawal_amount % 100

# def balance(with_drawal_amount , account_balance):
#     if value == 0 and  with_drawal_amount <= account_balance:
#         print(f"New balance = {account_balance - with_drawal_amount} ")
#     else:
#         print("Error")
# balance(with_drawal_amount , account_balance)

# Password Strength Checker
# Take a password string and check:
# Length ≥ 8
# Has at least one uppercase letter
# Has at least one lowercase letter
# Has at least one digit
# Has at least one special character (!@#$%^&*)


# #Password Strength Checker
# #Take a password string and check:
# #Length ≥ 8
# #Has at least one uppercase letter
# #Has at least one lowercase letter
# Has at least one digit
# Has at least one special character (!@#$%^&*)

# password = input("Enter the password: ")


# def len_password(password):
#     if len(password) >= 8:
#        print("It got a correct length")
#     else:
#         print("There should be more characters")

# def upper_case(password):
#     if not password.swapcase():
#         print("There should be a uppercase")
#     else: 
#         print("You are correct")
# def lower_case(password):
#     if not password.swapcase():
#         print("There should be a lowercase")
#     else:
#         print("You are correct")







# def special_characters(password):
#     if not password.isascii():
#         print("There should be a special character")
#     else:
#         print("You are correct")


# len_password(password)
# upper_case(password)
# lower_case(password)
# digit(password)
# special_characters(password)

# Bus Ticket Discount
# Input passenger’s age and whether they are a student (yes/no).
# If age < 12 → 50% discount
# If student → 30% discount
# If age > 60 → 40% discount
# Apply only one highest discount

# age = (int(input("Enter your age: ")))

# if age < 12:
#     print("You got 50% dicount ")
# elif age > 60:
#      print("You got 40% dicount ")
     
# student = (input("Are you student? "))

# if student == "yes" :
#     print("You got 30% dicount ")

# elif age < 12 and student == "yes":
#      print("You got 30% dicount")

# else :
#      print("You don't have any discounts ")


# Number in Range with Exceptions
# Take a number from the user and check:
# If it’s between 50 and 100 inclusive
# But also check if it’s not equal to 75 or 88 (skip those)

i = int(input("Enter a number between 50 to 100: "))

while 50<= i <= 100:

    if i == 75 or i == 88:
        print("The number is invalid")
        break 
    else:
        print("You did it ")
        break



