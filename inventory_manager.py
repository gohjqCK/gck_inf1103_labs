import json

class product:
    def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
    
    def update_stock():
        if Cinventory == []:
            return "empty"
        else:
            id = input("Enter Product ID: ")
            try:
                selectID = int(id.replace("P", "")) - 1
                try:
                    print("\nProduct Found:\nName: " + Cinventory[selectID]["NAME"])
                    print("Current Stock: " + str(Cinventory[selectID]["STOCK"]))
                except:
                    return "exist"
                newStock = int(input("\nNew stock quantity: "))         
                try:
                    Cinventory[selectID]["STOCK"] = newStock
                except:
                    return "fail"
            except ValueError:
                return "fail"

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")

class inventory:
    def __init__(self):
        self.products = {}

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

    def calculate_tax(self, amount):
        tax_rate = 0.07  # 7% sales tax
        tax_amount = amount * tax_rate
        total_with_tax = amount + tax_amount
        return total_with_tax

    def process_delivery(self, product_id, quantity):
        product = self.search_product(product_id)
        if product:
            product.update_stock(quantity)
            return product.price * quantity
        else:
            print("Product not found.")
            return 0
        
    def search_product(self, product_id):
        return self.products.get(product_id, None)

    def display_all():
        for product in Cinventory:
            output = f"ID: {product['ID']} | Name: {product['NAME']} | Price: {product['PRICE']} | Stock: {product['STOCK']}"
            print(output)

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
        Cinventory.extend(data)
    except FileNotFoundError:
        print("\nFile does not exist! Generating a new inventory file.\n")
        open('inventory.json', 'w+')

def search_product():
    id = input("Enter Product ID: ")
    try:
        selectID = int(id.replace("P", "")) - 1
        try:
            print("\nProduct Found:")
            print("-----------------------")
            print("ID: " + str(Cinventory[selectID]["ID"]))
            print("NAME: " + str(Cinventory[selectID]["NAME"]))
            print("PRICE: " + str(Cinventory[selectID]["PRICE"]))
            print("STOCK: " + str(Cinventory[selectID]["STOCK"]))
            print("-----------------------\n")

        except:
            return "exist"
    except ValueError:
        return "fail"

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
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

Cinventory = []

print("==================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==================================")

load_inventory()

while True:
    menu()
    option = choiceValidator(input("Enter Option: "))
    if option == "fail":
        print("WARNING: Please input a valid option")
    if option == 1:
        print("Current Inventory:\n")
        print("----------------------------------------------------")
        inventory.display_all()
        print("----------------------------------------------------\n")
        input("Press any key to continue...")

    if option == 2:
        print("\nAdd New Product")
        newprod = inventory.add_product()
        if newprod == "fail":
            print("One or more options invalid. Please try again.")
        elif newprod == "exist":
            print("Item ID already exists. Please try again.")
        else:
            print("\nProduct Added Successfully!\n")
            Cinventory.append(newprod)
            input("Press any key to continue...")

    if option == 3:
        print("\nUpdate Stock")
        upd = product.update_stock()
        if upd == "empty":
            print("\nNo products in stock\n")
        elif upd == "fail":
            print("\nInvalid input. Please try again.\n")
        elif upd == "exist":
            print("\nSpecified ID does not exist. Please try again.\n")
        else:
            print("\nStock Updated Successfully!\n")
            input("Press any key to continue...")

    if option == 4:
        print("\nSearch Product")
        search = search_product()
        if search == "fail":
            print("Invalid input. Please try again\n")
        elif search == "exist":
            print("Product not found. Please try again\n")
            input("Press any key to continue...")

    if option == 5:
        save_inventory(Cinventory)

    if option == 6:
        print("\nSaving inventory before exit...")
        save_inventory(Cinventory)
        print("\nInventory saved successfully.\n")
        print("Thank you for using the Inventory Management System\nProgram Terminated.")
        break