def get_valid_input(inventoryI):
    try:
        if inventoryI.isdigit() and int(inventoryI) > 0:
            inventoryI = inventoryI
        elif inventoryI.lower() == "quit":
            inventoryI = "quit"
        elif inventoryI.lower() == "report":
            inventoryI = "report"
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

file = open("history.txt", 'w')
orders = ['1001, Wireless Mouse, 2\n',
        '1002, Keyboard, 1\n',
        '1003, USB Cable, 3\n']

inventory = 0
total = 0
fail = 0

while True:
    inventoryI = input("Enter inventory amount: ")
    if get_valid_input(inventoryI).lower() == "quit":
        print("Quitting..")
        break

    else:
        if get_valid_input(inventoryI).isdigit():
            inventory = int(get_valid_input(inventoryI))
            total = int(process_delivery(inventory, total))
            price = calculate_tax(total)
            print(str(total) + " amount of units, total price is: $" + str(price))

        elif get_valid_input(inventoryI) == "fail":
            fail += 1
            print("Please input a valid number!")

        elif get_valid_input(inventoryI) == "report":
            generate_reports(total, fail)
            break