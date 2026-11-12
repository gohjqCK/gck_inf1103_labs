import json
from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct
from Modules.Inventory import Inventory
from Modules.Menu import Menu
from Modules.Supplier import Supplier

def load_inventory():
    try:
        open('inventory.json', 'r+')
        print("\ninventory.json found.\nInventory loaded successfully.\n")
        data = json.load(open('inventory.json', 'r+'))
        for item in data:
            if item["TYPE"] == "physical":
                store.products[item["ID"]] = PhysicalProduct(
                    product_id=item["ID"],
                    name=item["NAME"],
                    price=item["PRICE"],
                    stock=item["STOCK"],
                    itemType=item["TYPE"],
                    other_info=item["OTHER"],
                    supplier=Supplier(
                        supplier_id=item["SUPPLIERID"],
                        supplier_name=item["SUPPLIERNAME"],
                        supplier_email=item["SUPPLIEREMAIL"]
                    )
                )
            elif item["TYPE"] == "digital":
                store.products[item["ID"]] = DigitalProduct(
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
        newprod = Inventory.add_product(store)
        if newprod == "fail":
            print("One or more options invalid. Please try again.")
        elif newprod == "exist":
            print("Item ID already exists. Please try again.")
        elif newprod == "success":
            print("\nProduct Added Successfully!\n")
            input("Press any key to continue...")

    if option == 3:
        print("\nRemove Product")
        productID = input("Enter Product ID: ")
        fullID = f"P{int(productID.upper().replace('P', '')):03d}"
        remove = Inventory.remove_product(store, fullID)
        if remove == "fail":
            print("Product not found. Please try again.\n")
            input("Press any key to continue...")
        elif remove == "success":
            print("\nProduct removed successfully!\n")
            input("Press any key to continue...")

    if option == 4:
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

    if option == 5:
        print("\nSearch Product")
        inputID = input("Enter Product ID: ")
        productID = f"P{int(inputID.upper().replace('P', '')):03d}"
        search = Inventory.search_product(store, productID)
        if search == "fail":
            print("Invalid input. Please try again\n")
        elif search == "exist":
            print("Product not found. Please try again\n")
            input("Press any key to continue...")

    if option == 6:
        save_inventory(store.products)

    if option == 7:
        print("\nSaving inventory before exit...")
        save_inventory(store.products)
        print("\nInventory saved successfully.\n")
        print("Thank you for using the Inventory Management System\nProgram Terminated.")
        break