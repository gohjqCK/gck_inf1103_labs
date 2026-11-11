class Menu:
    def main_menu():
        print("-----------MENU-----------")
        print("1. Display all products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Update Stock")
        print("5. Search Product")
        print("6. Save inventory")
        print("7. Exit")
        print("--------------------------")

    def banner():
        print("==================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("==================================")

    def choiceValidator(choice):
        try:
            choice = int(choice)
            if choice < 1 or choice > 7:
                choice = "fail"
                return choice
            else:
                choice = choice
                return choice

        except ValueError:
            choice = "fail"
            return choice