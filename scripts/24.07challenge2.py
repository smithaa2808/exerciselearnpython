#Write a function print_table(number) that prints the table up to 10.
#print_table(5)
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

#instructions
# step1 defining the function print_table with one argument number
# step2 introducing "for" loop with range 
# step3 calling the function


def print_table(number):
    for i in range(1,11):
        print(number," x ", i, "=" ,number * i )
print_table(5) 

