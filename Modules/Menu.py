class Menu:
    @staticmethod
    def main_menu() -> None:
        print("-----------MENU-----------")
        print("1. Display all products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Update Stock")
        print("5. Search Product")
        print("6. Manage Orders")
        print("7. Save inventory")
        print("8. Exit")
        print("--------------------------")

    @staticmethod
    def banner() -> None:
        print("==================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("==================================")

    def choiceValidator(choice : int) -> int:
        try:
            choice = int(choice)
            if choice < 1 or choice > 8:
                choice = "fail"
                return choice
            else:
                choice = choice
                return choice

        except ValueError:
            choice = "fail"
            return choice