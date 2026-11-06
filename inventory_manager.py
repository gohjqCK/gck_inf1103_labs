import json
from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct
from Modules.Inventory import Inventory
from Modules.Menu import Menu

def load_inventory():
    try:
        open('inventory.json', 'r+')
        print("\ninventory.json found.\nInventory loaded successfully.\n")
        data = json.load(open('inventory.json', 'r+'))
        for item in data:
            if item["TYPE"] == "physical":
                store.products[item["ID"]] = PhysicalProduct(
                    item["ID"],
                    item["NAME"],
                    item["PRICE"],
                    item["STOCK"],
                    item["TYPE"],
                    item["OTHER"]
                )
            else:
                store.products[item["ID"]] = DigitalProduct(
                    item["ID"],
                    item["NAME"],
                    item["PRICE"],
                    item["STOCK"],
                    item["TYPE"],
                    item["OTHER"]
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
            "STOCK": p.stock,
            "TYPE": p.itemType,
            "OTHER": p.weight if isinstance(p, PhysicalProduct) else p.download_size
        }
        for p in inventory.values()
    ]
    with open("inventory.json", "w") as file:
        json.dump(item, file)
    print("Inventory saved successfully.\n")

store = Inventory()
load_inventory()

while True:
    Menu.banner()
    Menu.main_menu()
    option = Menu.choiceValidator(input("Enter Option: "))
    if option == "fail":
        print("WARNING: Please input a valid option")
    if option == 1:
        print("Current Inventory:\n")
        print("----------------------------------------------------")
        Inventory.display_information(store)
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