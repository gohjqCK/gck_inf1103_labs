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

    def main_menu(self):
        print("-----------MENU-----------")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        print("--------------------------")

    def banner(self):
        print("==================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("==================================")

    def choiceValidator(self, choice):
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