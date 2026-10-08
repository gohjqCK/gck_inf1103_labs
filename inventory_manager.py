def choiceValidator(choice):
    try:
        choice = int(choice)
        if choice < 1 or choice > 6:
            choice = "fail"
            return choice
        else:
            choice = choice
            return choice

    except ValueError:
        choice = "fail"
        return choice

def add_product():
    try:
        itemID = int(input("Product ID: "))
        itemName = input("Product Name: ")
        itemPrice = int(input("Price: "))
        itemStock = int(input("Stock Quantity: "))
    except ValueError:
        return "fail"
    if input:
        item = {
            "ID" : itemID, 
            "NAME" : itemName, 
            "PRICE" : itemPrice, 
            "STOCK" : itemStock
            }
        return item
    else:
        return "fail"


Cinventory = []
print("==================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==================================")


print(
    "-----------MENU-----------\n" + 
    "1. Display all products\n" +
    "2. Add product\n" +
    "3. Update Stock\n" +
    "4. Search Product\n" +
    "5. Save inventory\n" +
    "6. Exit\n" +
    "--------------------------"
    )

while True:

    option = choiceValidator(input("Enter Option: "))
    if option == "fail":
        print("WARNING: Please input a valid option")
    if option == 1:
        print("Current Inventory:\n")
    if option == 2:
        newprod = add_product()
        if newprod == "fail":
            print("One or more options invalid. Please try again.")
        else:
            print("\nProduct Added Successfully!\n")
            Cinventory.append(newprod)
            print(Cinventory)