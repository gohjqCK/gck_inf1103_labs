inventory = 0
while True:
    try:
        inventoryI = int(input("Enter inventory amount: "))

        if str(inventory).isdigit() and inventoryI > 0:
            if inventory >= 0:
                inventory = inventory + inventoryI
                print("Current inventory amount is: " + str(inventory))
            elif inventory <= 0:
                print("Please enter a valid number!")
        else:
            print("Please enter a valid number!")

    except ValueError:
        print("Please enter a valid number!")

