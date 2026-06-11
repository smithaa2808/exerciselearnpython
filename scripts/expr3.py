def racing(laps):
    i = 5
    total = []

    while i < laps:
        print(f"Adding {i} to the list")
        total.append(i)
        i = i + 1
    print("This is not the correct number", total)
racing(10)

