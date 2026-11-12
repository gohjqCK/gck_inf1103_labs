import json
from Modules.Product import Product
from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct
from Modules.Inventory import Inventory
from Modules.Menu import Menu
from Modules.Supplier import Supplier
from Modules.Order import Order
from Modules.Orderline import Orderline

def load_inventory():
    try:
        open('inventory.json', 'r+')
        print("\ninventory.json found.\nInventory loaded successfully.\n")
        data = json.load(open('inventory.json', 'r+'))
        for item in data:
            itemType = item.get("TYPE")
            if itemType == "physical":
                product = PhysicalProduct(
                    product_id=item["ID"],
                    name=item["NAME"],
                    price=float(str(item["PRICE"]).replace("$", "")),
                    stock=item["STOCK"],
                    itemType=item["TYPE"],
                    other_info=item["OTHER"],
                    supplier=Supplier(
                        supplier_id=item["SUPPLIERID"],
                        name=item["SUPPLIERNAME"],
                        contact_email=item["SUPPLIEREMAIL"]
                    )
                )
                store.products.append(product)

            elif itemType == "digital":
                product = DigitalProduct(
                    product_id=item["ID"],
                    name=item["NAME"],
                    price=float(str(item["PRICE"]).replace("$", "")),
                    stock=item["STOCK"],
                    itemType=item["TYPE"],
                    other_info=item["OTHER"],
                    supplier=Supplier(
                        supplier_id=item["SUPPLIERID"],
                        name=item["SUPPLIERNAME"],
                        contact_email=item["SUPPLIEREMAIL"]
                    )
                )
                store.products.append(product)

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
            "OTHER": p.other_info,
            "SUPPLIERID": p.supplier.supplier_id,
            "SUPPLIERNAME": p.supplier.name,
            "SUPPLIEREMAIL": p.supplier.contact_email
        }
        for p in inventory
    ]
    with open("inventory.json", "w") as file:
        json.dump(item, file)
    print("\nInventory saved successfully.\n")

store = Inventory()
orders = {}
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
        store.display_information()
        print("----------------------------------------------------\n")

    if option == 2:
        print("\nAdd New Product")
        try:
            productID = input("Product ID: ")
            fullID = f"P{int(productID.upper().replace('P', '')):03d}"
            if any(product.product_id == fullID for product in store.products):
                input("Item already exists. Please try again...\n")
                continue
            itemName = input("Product Name: ")
            itemPrice = float(input("Price: "))
            itemStock = int(input("Stock Quantity: "))
            itemType = input("Product Type (Physical/Digital): ").strip().lower()
            if itemType == "physical":
                itemWeight = float(input("Weight in Kgs: "))
            elif itemType == "digital":
                itemDownloadSize = float(input("Download Size in MB: "))
            supplyID = input("Supplier ID: ")
            supplyName = input("Supplier Name: ")
            supplyEmail = input("Supplier Contact Email: ")
            supplier = Supplier(supplyID, supplyName, supplyEmail)
            if itemType == "physical":
                product = PhysicalProduct(fullID, itemName, itemPrice, itemStock, supplier, itemType, itemWeight)
                store.add_product(product)
                input("\nSuccessfully added product! Press any key to continue...\n")
            elif itemType == "digital":
                product = DigitalProduct(fullID, itemName, itemPrice, itemStock, supplier, itemType, itemDownloadSize)
                store.add_product(product)
                input("\nSuccessfully added product! Press any key to continue.\n")
        except ValueError:
                    print("Invalid input, please try again.\n")
                    
    if option == 3:
        print("\nRemove Product")
        try:
            productID = input("Enter Product ID: ")
            fullID = f"P{int(productID.upper().replace('P', '')):03d}"
        except ValueError:
            print("Invalid input, please input a valid number")
            continue
        remove = store.remove_product(store, fullID)
        if remove == "fail":
            print("Product not found. Please try again.\n")
            input("Press any key to continue...")
        elif remove == "success":
            print("\nProduct removed successfully!\n")
            input("Press any key to continue...")

    if option == 4:
        print("\nUpdate Stock")
        try:
            productID = input("Enter Product ID: ")
            fullID = f"P{int(productID.upper().replace('P', '')):03d}"
            item = store.search_product(fullID, "upd")
            try:
                product = store.find_product(fullID)
                newStock = int(input("Enter new stock quantity: "))
                product.update_stock(newStock)
                print("\nStock updated successfully!\n")
                input("Press any key to continue...")
            except ValueError:
                print("Invalid stock quantity. Please try again.\n")
        except ValueError:
            print("Invalid input, please input a valid number")
            continue

    if option == 5:
        print("\nSearch Product")
        try:
            productID = input("Enter Product ID: ")
            fullID = f"P{int(productID.upper().replace('P', '')):03d}"
        except ValueError:
            print("Invalid input, please input a valid number\n")
            continue
        search = store.search_product(fullID, "search")
        if search == "fail":
            print("Product not found or Invalid ID. Please try again\n")

    if option == 6:
        print("--------------------------\n1. Add Order\n2. Remove Order\n3. View Orders\n4. Exit to main menu")
        try:
            choice = int(input("Enter Option: "))
        except ValueError:
            print("WARNING: Please put a valid option")
        print("--------------------------")

        if choice == 1:
            print("\nAdd Order")
            orderID = input("Enter Order ID: ")
            if orderID in orders:
                order = orders[orderID]
            else:
                order = Order(orderID)
                orders[orderID] = order
            try:
                productID = input("Enter Product ID: ")
                fullID = f"P{int(productID.upper().replace('P', '')):03d}"
            except ValueError:
                print("Invalid number, please try again.")
                continue
            product = store.find_product(fullID)
            if product is None:
                print("Product does not exist, please try again.")
                continue
            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid input, please try again")
                continue

            order.add_order_line(product, quantity)
            print("\nOrder successfully added!")
            continue

        elif choice == 2:
            if not orders:
                print("No orders yet, no orders to remove.\n")
                continue
            orderID = input("Enter an Order ID to remove from: ")
            if orderID in orders:
                order = orders[orderID]
            else:
                order = Order(orderID)
                orders[orderID] = order
            try:
                productID = input("Enter a Product ID to remove from the Order: ")
                fullID = f"P{int(productID.upper().replace('P', '')):03d}"
            except ValueError:
                print("Invalid input, please try again.")
            remove = order.remove_order_line(fullID)
            if remove == "success":
                print("Order Line successfully removed.")
            else:
                print("Product is not in this Order.")

        elif choice == 3:
            if not orders:
                print("No orders yet, add an order.\n")
            else:
                for orderID, order in orders.items():
                    order.view_order()
            input("Press any key to continue")
        
        elif choice == 4:
            print("Returning to main menu.")
            continue

        else:
            print("Pick a valid choice (1 - 3)")
    
    if option == 7:
        save_inventory(store.products)

    if option == 8:
        print("\nSaving inventory before exit...")
        save_inventory(store.products)
        print("Thank you for using the Inventory Management System\nProgram Terminated.")
        break