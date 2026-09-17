inventory = 0
while True:
    inventoryI = input("Enter inventory amount: ")

    if inventoryI.lower() == "quit":
        print("Quitting. Final inventory number is: " + str(inventory))
        break
    try:
        if str(inventory).isdigit() and int(inventoryI) > 0:
            if inventory >= 0  and inventory < 501:
                inventory += int(inventoryI)
                if inventory < 501:
                    print("Current inventory amount is: " + str(inventory))
                else:
                    print("ALERT! Current inventory is: " + str(inventory) + "! " + str(inventory - 500) + " over the alllowed limit!")
                    quit()
            elif inventory <= 0:
                print("Please enter a valid number!")
        else:
            print("Please enter a valid Number!")
    except ValueError:
        print("Please enter a valid number!")