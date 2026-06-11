#Print numbers from 1 to 10 using a loop.
#Store 5 fruits in a list and print the second one.
#Loop through the list and print each fruit in uppercase.
#Sum all numbers in a list using a loop.
#Create a multiplication table for a number given by the user.

numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(0,10):
    print(f"The number is {i}")


fruits = ["apricots", "Berries", "cherry", "Fig", "Amala"] 
print(fruits[1])

for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()
print(fruits)

total = 0
for j in numbers:
    value = int(j)
    print(value)
    total += value
print(total)

integer = int(input('Enter a number: '))

def table(number):
    for i in range(1,11):
        print(number,'x',i,'=',number * i)

table(integer)










