print("This is about coding ") 
print("The level of coding can be basic , intermediate and advanced ")

while True:
    level = input("What's your level in coding?")

    if level == "basic":
        print("You can solve basic problems")
        exit()

    elif level == "intermediate":
        print("You can solve many problems")
    
    elif level == "advanced":
        print("You can solve any problems")

    else:
        print("You have to learn coding")
        exit()