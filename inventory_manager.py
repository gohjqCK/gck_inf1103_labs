import json

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

# def display_all():

def add_product():
    try:
        itemID = int(input("Product ID: "))
        fullID = f"P{itemID:03d}"
        if any(item['ID'] == fullID for item in Cinventory):
                return "exist"  
        itemName = input("Product Name: ")
        itemPrice = float(input("Price: "))
        itemStock = int(input("Stock Quantity: "))
    except ValueError:
        return "fail"
    fullPrice = f"${itemPrice:.2f}"     
    item = {
        "ID" : fullID, 
        "NAME" : itemName, 
        "PRICE" : fullPrice, 
        "STOCK" : itemStock
        }
    return item
        
def update_stock():
    if Cinventory == []:
        return "empty"
    else:
        id = input("Enter Product ID: ")
        try:
            selectID = int(id.replace("P", "")) - 1
            newStock = int(input("New stock quantity: "))         
            try:
                Cinventory[selectID]["STOCK"] = newStock
            except:
                return "fail"
        except ValueError:
            return "fail"
        
Cinventory = [
    {'ID': 'P001', 'NAME': 'Laptop', 'PRICE': '$1200.00', 'STOCK': 15},
    {'ID': 'P002', 'NAME': 'Mouse', 'PRICE': '$25.50', 'STOCK': 40},
    {'ID': 'P003', 'NAME': 'Keyboard', 'PRICE': '$45', 'STOCK': 25}
]

print("==================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==================================")

# try:
#     file = open('inventory.json', 'w+')
#     try:
        
#     except:
#         print("Inventory failed to load.")
#     print("\ninventory.json found.\nInventory loaded successfully.\n")
# except:
#     print("Failed to locate inventory.json")

print(
    "-----------MENU-----------\n" + 
    "1. Display all products\n" +
    "2. Add product\n" +
    "3. Update Stock\n" +
    "4. Search Product\n" +
    "5. Save inventory\n" +
    "6. Exit\n" +
    "--------------------------\n"
    )

while True:

    option = choiceValidator(input("Enter Option: "))
    if option == "fail":
        print("WARNING: Please input a valid option")
    if option == 1:
        print("Current Inventory:\n")
        print("----------------------------------------------------")
        for product in Cinventory:
            output = f"ID: {product['ID']} | Name: {product['NAME']} | Price: {product['PRICE']} | Stock: {product['STOCK']}"
            print(output)
        print("----------------------------------------------------\n")

    if option == 2:
        print("\nAdd New Product")
        newprod = add_product()
        if newprod == "fail":
            print("One or more options invalid. Please try again.")
        elif newprod == "exist":
            print("Item ID already exists. Please try again.")
        else:
            print("\nProduct Added Successfully!\n")
            Cinventory.append(newprod)
    if option == 3:
        upd = update_stock()
        if upd == "empty":
            print("\nNo products in stock\n")
        elif upd == "fail":
            print("\nInvalid ID. Please try again.\n")
        elif upd == "exist":
            print("\nSpecified ID does not exist. Please try again.\n")
        else:
            print("\nStock Updated Successfully!\n")