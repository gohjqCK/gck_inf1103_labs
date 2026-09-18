def get_valid_input(inventoryI):
    if inventoryI.isdigit() and int(inventoryI) > 0:
        inventoryI = inventoryI
    elif inventoryI.lower() == "quit":
        inventoryI = "quit"
    else:
        inventoryI = "Please input a valid number"
    return inventoryI

def process_delivery(current_value, total_value):
    total_value = current_value + total_value
    return total_value

def calculate_tax(amount):
    print("hi")