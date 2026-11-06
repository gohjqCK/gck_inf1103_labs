class Menu:
    def __init__(self):
        self.options = [
            "Display all products",
            "Add product",
            "Update Stock",
            "Search Product",
            "Save inventory",
            "Exit"
        ]

    def main_menu():
        print("-----------MENU-----------")
        print("1. Display all products")
        print("2. Add product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save inventory")
        print("6. Exit")
        print("--------------------------")

    def banner():
        print("==================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("==================================")

    def choiceValidator(choice):
        try:
            choice = int(choice)
            if choice < 1 or choice > 6:
                choice = "fail"
                return choice
            else:
                choice = choice
                return choice

        except ValueError:
            choice = "fail"
            return choice