cars = 100  # assigning values to cars 
space_in_a_car = 4.0 # assigning values to space_in_a_car 
drivers = 30 # assigning values to drivers 
passengers = 90 # assigning values to passengers 
cars_not_driven = cars - drivers  # cars_not_driven is subtracted drivers from cars 
cars_driven = drivers  # drivers are assigned to cars_driven
carpool_capacity = cars_driven * space_in_a_car # carpool_capacity is multiplication of cars_driven and space_in_a_car 
average_passengers_per_car = passengers / cars_driven # average_passengers_per_car is division of passengers and car_driven 

print("There are", cars, " cars available.") # we are printing variable cars along with text as string 
print("There are only", drivers, "drivers available.") # we are printing variable drivers along with text as string 
print("There will be", cars_not_driven, "empty cars today.") # we are printing variable cars_not_drivers along with text as string 
print("We can transport", carpool_capacity, "people today.") # we are printing variable carpool_capacity along with text as string
print("We have", passengers, "to carpool today.") # we are printing variable passengers along with text as string
print("We need to put about", average_passengers_per_car,"in each car.") # we are printing variable average_passengers_per_car along with text as string

white_balls = 300
black_balls = 500
red_balls = black_balls - white_balls
brown_balls = red_balls * black_balls - white_balls
green_balls = white_balls / brown_balls + black_balls

print("Pinky have", green_balls , "balls she is happy with it")
print("Harry have", brown_balls, "balls he hided all the balls")
print("Wosely have", red_balls, " balls he gave to harry ")
print("Granger have", black_balls, "balls she losed everything")
print(" total balls left over ", white_balls + black_balls + brown_balls + red_balls + green_balls)