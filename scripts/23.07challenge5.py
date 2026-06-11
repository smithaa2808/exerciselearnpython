#marks = [88, 76, 90, 65, 70]

#average_marks = sum(marks) / len(marks)

#highest = max(marks)
#lowest = min(marks)

#print("The average mark is", average_marks)
#print("The highest mark is", highest)
#print("The lowest mark is ", lowest)

marks = [88, 76, 90, 65, 70]

total = 0  # assigning value for total
highest = marks[0]  # It will be assigned to the 1st number 
#print(highest)
lowest = marks[0] # It will assigned to 1st number
#print(lowest)

for mark in marks:
    print(mark)
    total += mark

#print(total) # prints the sum of mark in the list
    if mark > highest:
       highest = mark 
#print(highest)

    if mark < lowest:
       lowest = mark
#print(lowest)

average = total / len(marks)
#print(average)
print("Average Marks:", round(average, 1))  # this will round off the decimal number 
print("Highest:", highest)
print("Lowest:", lowest)



