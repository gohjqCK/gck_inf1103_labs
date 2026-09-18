import processes

inventory = 0
total_value = 0
while True:
    inventoryI = input("Enter inventory amount: ")
    if processes.get_valid_input(inventoryI).lower() == "quit":
        print("Quitting..")
        break
    else:
        inventory = processes.get_valid_input(inventoryI)
        processes.process_delivery(inventory, total_value)

    # try:
    #     if str(inventory).isdigit() and int(inventoryI) > 0:
    #         if inventory >= 0  and inventory < 501:
    #             inventory += int(inventoryI)
    #             if inventory < 501:
    #                 print("Current inventory amount is: " + str(inventory))
    #             else:
    #                 print("ALERT! Current inventory is: " + str(inventory) + "! " + str(inventory - 500) + " over the alllowed limit!")
    #                 quit()
    #         elif inventory <= 0:
    #             print("Please enter a valid number!")
    #     else:
    #         print("Please enter a valid Number!")
    # except ValueError:
    #     print("Please enter a valid number!")