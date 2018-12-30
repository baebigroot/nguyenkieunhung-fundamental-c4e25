items = ["T-shirt", "Sweater"]

loop = True

while loop:
    order = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    
    if order == "R" or order == "r":
        print("Our items: ", end = "")
        print(*items, sep=", ")
    
    
    elif order == "C" or order == "c":
        y = input("Enter new item: ")
        items.append(y)
        print("Our items: ", end = "")
        print(*items, sep=", ")
   
   
    elif order == "U" or order == "u":
        x = int(input("Update position ?"))
        y = str(input("New item ? "))
        items[x - 1] = y
        print("Our items: ", end = "")
        print(*items, sep=", ")
     
    
    elif order == "D" or order == "d":
        x = int(input("Delete position ? "))
        items.pop(x - 1)
        print("Our items: ", end = "")
        print(*items, sep=", ")
        loop = False

