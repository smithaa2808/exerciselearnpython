def cheese_and_crackers(cheese_count, boxes_of_crackers): # defining a function which have 2 variables 
    print(f"You have {cheese_count} cheeses!") # Prints the mesaage that have the value of the variable
    print(f"You have {boxes_of_crackers} boxes of crackers!") # prints the messsage that have the value of the varible
    print("Man that's enough for a party!") # displays the message on the screen
    print("Get a blanket.\n") # displays message on the screen and \n is meant to continue the text in next line

print("We can just give the function numbers directly:") # displays message to the user
cheese_and_crackers(10, 5) # Runs cheese_and_crackers function but doesn't pass any parameters 


print("OR, we can use variables from pur script:") # displays message to the user
amount_of_cheese = 10 # stores the no of cheese units
amount_of_crackers = 50 # stores the no of crackers

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # Runs the cheese_and_crackers function using 10 forcheese and 5 for crackers


print("We can even do math inside to:") # displays he message to the user
cheese_and_crackers(10 + 20, 5 + 6) # Runs cheese_and_crackers function with 30 , 11 


print("And we can combine the two, variables and math:") # displays the message to the user ``
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000) #Runs the function with numbers amount_of_cheese + 100 and amount_of_crackers + 1000
