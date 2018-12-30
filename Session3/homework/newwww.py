store_items = ["T-shirt", "Sweater"]
items = ""
check = "y"
while (check == "y" or check == "Y"):
    cus_order = input("Welcome to our shop, choose an oder(C,R,U,D)  :") 
    # Read all the items
    if cus_order == "r" or cus_order == "R" :
        for (i,val) in enumerate(store_items):
            items += val
            if i < len(store_items)-1: items += ","
            else : items +="."
        print("Our items:",items)
    # Create an item
    elif cus_order =="c" or cus_order =="C" :
        new_item_upper = input("Enter new item:")
        new_item = new_item_upper.title()
        store_items.append(new_item)
        items =""
        for (i,val) in enumerate(store_items):
            items += val
            if i < len(store_items)-1: items += ","
            else:items +="."
        print("Our items:",items)
    # Update items
    elif cus_order =="u" or cus_order == "U" :
        pos_update = int(input("Update Position? "))
        while (pos_update > len(store_items)):
            print("You must enter a number lower or equal",len(store_items))
            pos_update = int(input("Update Position? "))
        new_item_upper = input("Enter new item:")
        new_item = new_item_upper.title()
        store_items[pos_update-1] = new_item
        items =""
        for (i,val) in enumerate(store_items):
            items += val
            if i < len(store_items)-1: items += ","
            else : items +="."
        print("Our items:",items)
    # Delete items
    else:
        pos_delete = int(input("Delete Position? "))
        while pos_delete > len(store_items):
            print("You must enter a number lower or equal",len(store_items))
            pos_delete = int(input("Delete Position? "))
        del store_items[pos_delete-1]
        items =""
        for (i,val) in enumerate(store_items):
            items += val
            if i < len(store_items)-1: items += ","
            else: items += "."
        print("Our items:",items)

    check = input("continue(Y or N):") 