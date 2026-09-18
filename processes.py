def get_valid_input(inventoryI):
    if inventoryI.isdigit() and int(inventoryI) > 0:
        inventoryI = inventoryI
    elif inventoryI.lower() == "quit":
        inventoryI = "quit"
    else:
        inventoryI = "Please input a valid number"
    return inventoryI

def process_delivery(current_total, new_value):
    new_value += current_total
    return new_value

def calculate_tax(amount):
    price = 0.50
    full_cost = amount * price
    discount = full_cost * 0.9
    return discount

def generate_reports(total_units, failed_attempts):
    print("hi")