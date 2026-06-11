if __name__ == "__main__":
    item = 0
    price = 0

while True:
    cost = input("Enter the item price:")
    if cost == "done":
       break
    cost = int(cost)
    item += 1
    price += cost 

print("Total items", item)
print("Total cost", price)

           


