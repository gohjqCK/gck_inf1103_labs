inventory = 0
while True:
    try:
        inventoryI = int(input("Enter inventory amount: "))

        if str(inventory).isdigit() and inventoryI > 0:
            if inventory >= 0  and inventory < 500:
                inventory = inventory + inventoryI
                if inventory < 500:
                    print("Current inventory amount is: " + str(inventory))
                else:
                    print("Current inventory amount is: " + str(inventory))
                    print("ALERT! Inventory over 500! Ending program...")
                    quit()
            elif inventory <= 0:
                print("Please enter a valid number!")
        
        else:
            print("Please enter a valid Number!")

    except ValueError:
        print("Please enter a valid number!")

