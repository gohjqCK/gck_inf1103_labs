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
                    price=item["PRICE"],
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
                    price=item["PRICE"],
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
        store.display_information()
        print("----------------------------------------------------\n")
        # shipInfo = input("Press 1 to view shipping information, or any other key to continue. ")
        # if shipInfo == "1":
        #     for product in store.products.values():
        #         if product.get_fulfillment_info() == "physical":
        #             print(f"Product ID: {product.product_id} | Name: {product.name} | Fulfillment Info: {product.get_fulfillment_info()}")
        #             print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        #     print("----------------------------------------------------\n")
        #     input("Press any key to continue...")

    if option == 2:
        print("\nAdd New Product")
        try:
            itemID = int(input("Product ID: "))
            fullID = f"P{itemID:03d}"
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
            fullPrice = f"${itemPrice:.2f}"  
            if itemType == "physical":
                product = PhysicalProduct(fullID, itemName, fullPrice, itemStock, supplier, itemType, itemWeight)
                store.add_product(product)
                input("\nSuccessfully added product! Press any key to continue...\n")
            elif itemType == "digital":
                product = DigitalProduct(fullID, itemName, fullPrice, itemStock, supplier, itemType, itemDownloadSize)
                store.add_product(product)
                input("\nSuccessfully added product! Press any key to continue.\n")
        except ValueError:
                    print("Invalid input, please try again.\n")
                    
    if option == 3:
        print("\nRemove Product")
        try:
            itemID = int(input("Enter Product ID: "))
            fullID = f"P{itemID:03d}"
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
            productID = int(input("Enter Product ID: "))
            fullID = f"P{productID:03d}"
            item = store.search_product(fullID, "upd")
            try:
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
            inputID = int(input("Enter Product ID: "))
            fullID = f"P{inputID:03d}"
        except ValueError:
            print("Invalid input, please input a valid number\n")
            continue
        search = store.search_product(fullID, "search")
        if search == "fail":
            print("Product not found or Invalid ID. Please try again\n")

    if option == 6:
        print("\nAdd Order")
        print("==================================")
        while True:
            orderID = Order(input("\nEnter Order ID: "))
            productID = int(input("Enter Product ID: "))
            quantity = input("Enter Quantity: ")
            fullID = f"P{productID:03d}"
            try:
                quantity = int(quantity)
                orderID.add_order_line(fullID, quantity)
                print("\nOrder successfully added!")
            except ValueError:
                print("Invalid input, please try again")
            choice = input("\nPress any key to add another product, or enter 'exit' to go back to main menu: ")
            if choice.lower() == 'exit':
                break

    if option == 7:
        save_inventory(store.products)

    if option == 8:
        print("\nSaving inventory before exit...")
        save_inventory(store.products)
        print("\nInventory saved successfully.\n")
        print("Thank you for using the Inventory Management System\nProgram Terminated.")
        break