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