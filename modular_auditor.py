import processes

inventory = 0
total = 0
fail = 0

while True:
    inventoryI = input("Enter inventory amount: ")
    if processes.get_valid_input(inventoryI).lower() == "quit":
        print("Quitting..")
        break

    else:
        if processes.get_valid_input(inventoryI).isdigit():
            inventory = int(processes.get_valid_input(inventoryI))
            total = int(processes.process_delivery(inventory, total))
            price = processes.calculate_tax(total)
            print(str(total) + " amount of units, total price is: $" + str(price))

        elif processes.get_valid_input(inventoryI) == "fail":
            fail += 1
            print("Please input a valid number!")

        elif processes.get_valid_input(inventoryI) == "report":
            processes.generate_reports(total, fail)
            break