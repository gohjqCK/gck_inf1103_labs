import json

class product:
    def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
    
    def update_stock(self, itemStock):
        self.stock = itemStock

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} units")

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        try:
            itemID = int(input("Product ID: "))
            fullID = f"P{itemID:03d}"
            if fullID in self.products:
                    return "exist"  
            itemName = input("Product Name: ")
            itemPrice = float(input("Price: "))
            itemStock = int(input("Stock Quantity: "))
        except ValueError:
            return "fail"
        fullPrice = f"${itemPrice:.2f}"  
        self.products[fullID] = product(fullID, itemName, fullPrice, itemStock)   
        return "success"

    def search_product(self, productID):
        if productID in self.products:
            print("\nProduct Found:")
            print("-----------------------")
            print(f"ID: {self.products[productID].product_id} | Name: {self.products[productID].name} | "
                  f"Price: {self.products[productID].price} | Stock: {self.products[productID].stock}")
            print("-----------------------\n")
        elif productID not in self.products:
            return "exist"
        else:
            return "fail"
        return None

    def display_all(self):
        for product in self.products.values():
            print(f"ID: {product.product_id} | Name: {product.name} | "
                  f"Price: {product.price} | Stock: {product.stock}")
            
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

def load_inventory():
    try:
        open('inventory.json', 'r+')
        print("\ninventory.json found.\nInventory loaded successfully.\n")
        data = json.load(open('inventory.json', 'r+'))
        for item in data:
            store.products[item["ID"]] = product(
                item["ID"],
                item["NAME"],
                item["PRICE"],
                item["STOCK"],
            )
    except FileNotFoundError:
        print("\nFile does not exist! Generating a new inventory file.\n")
        open('inventory.json', 'w+')
    except json.JSONDecodeError:
        print("\nError decoding JSON. Please check the inventory.json file.\n")

def save_inventory(inventory):
    item = [
        {
            "ID": p.product_id,
            "NAME": p.name,
            "PRICE": p.price,
            "STOCK": p.stock
        }
        for p in inventory.values()
    ]
    with open("inventory.json", "w") as file:
        json.dump(item, file)
    print("Inventory saved successfully.\n")


def menu():
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

print("==================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==================================")

store = Inventory()
load_inventory()

while True:
    menu()
    option = choiceValidator(input("Enter Option: "))
    if option == "fail":
        print("WARNING: Please input a valid option")
    if option == 1:
        print("Current Inventory:\n")
        print("----------------------------------------------------")
        Inventory.display_all(store)
        print("----------------------------------------------------\n")
        input("Press any key to continue...")

    if option == 2:
        print("\nAdd New Product")
        newprod = Inventory.add_product(store)
        if newprod == "fail":
            print("One or more options invalid. Please try again.")
        elif newprod == "exist":
            print("Item ID already exists. Please try again.")
        elif newprod == "success":
            print("\nProduct Added Successfully!\n")
            input("Press any key to continue...")

    if option == 3:
        print("\nUpdate Stock")
        productID = input("Enter Product ID: ")
        fullID = f"P{int(productID.upper().replace('P', '')):03d}"
        item = store.search_product(fullID)
        if item is None:
            try:
                newStock = int(input("Enter new stock quantity: "))
                store.products[fullID].update_stock(newStock)
                print("\nStock updated successfully!\n")
                input("Press any key to continue...")
            except ValueError:
                print("Invalid stock quantity. Please try again.\n")


    if option == 4:
        print("\nSearch Product")
        inputID = input("Enter Product ID: ")
        productID = f"P{int(inputID.upper().replace('P', '')):03d}"
        search = Inventory.search_product(store, productID)
        if search == "fail":
            print("Invalid input. Please try again\n")
        elif search == "exist":
            print("Product not found. Please try again\n")
            input("Press any key to continue...")

    if option == 5:
        save_inventory(store.products)

    if option == 6:
        print("\nSaving inventory before exit...")
        save_inventory(store.products)
        print("\nInventory saved successfully.\n")
        print("Thank you for using the Inventory Management System\nProgram Terminated.")
        break