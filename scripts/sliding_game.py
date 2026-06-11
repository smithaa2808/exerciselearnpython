print("This is a sliding game.")

print("Kids have 4 choices, hold, push, slide, laugh")

# the game will happen multiple times. 

while True:

    play_choice = input("What you want to do? ")

    if play_choice == "slide":
        print("Enjoy Sliding..Laugh")
        exit()
    elif play_choice == "hold":
        print("Other kids push him...")
    elif play_choice == "push":
        print("Holding child is shouting...")
    else:
        print("The kids are waiting...")
