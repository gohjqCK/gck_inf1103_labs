def get_valid_input(inventoryI):
    try:
        if inventoryI.isdigit() and int(inventoryI) > 0:
            inventoryI = inventoryI
        elif inventoryI.lower() == "quit":
            inventoryI = "quit"
        elif inventoryI.lower() == "report":
            inventoryI = "report"
        elif inventoryI.lower() == "load":
            inventoryI = "load"
        elif inventoryI.lower == "save":
            inventoryI = "save"
        else:
            inventoryI = "fail"
    except ValueError:
        inventoryI = "fail"
    return inventoryI

def process_delivery(current_total, new_value):
    new_value += current_total
    return new_value

def calculate_tax(amount):
    price = 0.50
    full_cost = amount * price
    tax = full_cost * 1.1
    return tax

def generate_reports(total_units, failed_attempts):
    chit = print(str(total_units) + " amount of units total, " + str(failed_attempts) + " times failed during this request")
    return chit

def load_inventory():
    file.seek(0)
    status = file.readlines()
    print(status)
    return status


inventory = 0
total = 0
fail = 0
counter = 0
totalOrder = []
file = open("inventory.txt", 'r+')
orderlist = list(file.readlines())
for order in orderlist:
        counter += 1

while True:
    inventoryI = input("Enter Product Name: ")

    if get_valid_input(inventoryI).lower() == "quit":
        file.writelines(newOrder)
        file.close()
        print("Quitting..")
        break
    elif get_valid_input(inventoryI) == "load":
        print("All orders:")
        load_inventory()

    else:
        quantity = input("Enter Quantity: ")
        if get_valid_input(quantity).isdigit():
            inventory = int(get_valid_input(quantity))
            total = int(process_delivery(inventory, total))
            price = calculate_tax(total)
            #print(str(total) + " amount of units, total price is: $" + str(price))
            print("New order added:")
            newOrder = [counter + 1001, inventoryI, str(inventory) + "\n"]
            totalOrder += newOrder
            print(totalOrder)
            counter += 1

        elif get_valid_input(inventoryI) == "fail":
            fail += 1
            print("Please input a valid number!")

        elif get_valid_input(inventoryI) == "report":
            generate_reports(total, fail)
            break