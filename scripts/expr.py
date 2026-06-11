def circle(area):
    i = 3.14
    numbers = []

    while i < area:
        print(f"Adding {i} to the list.")
        numbers.append(i)
        i = i + 1

    print("The numbers: ", numbers)
circle(6)


def build_numbers_list(limit, step):
    i = 0
    numbers = []

    while i < limit:
        print(f"Adding {i} to the list.")
        numbers.append(i)
        i = i + step

    print("The numbers: ", numbers)
build_numbers_list(10, 2)


def build_numbers_list(limit, step):
    numbers = []

    for i in range(0, limit, step):
        print(f"Adding {i} to the list.")
        numbers.append(i)

    print("The numbers: ", numbers)
    
build_numbers_list(10,4)
