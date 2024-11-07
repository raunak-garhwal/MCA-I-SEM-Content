class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self) :
        return f"{self.name} : {self.description} -> Rs.{self.price}"


class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item, section="Miscellaneous"):
        if section not in self.menu_items:
            self.menu_items[section] = []
        self.menu_items[section].append(item)

    def remove_item(self, item_name):
        for section in self.menu_items:
            for item in self.menu_items[section]:
                if item.name == item_name:
                    self.menu_items[section].remove(item)
                    return True
        return False

    def update_price(self, item_name, new_price):
        for section in self.menu_items:
            for item in self.menu_items[section]:
                if item.name == item_name:
                    item.price = new_price
                    return True
        return False

    def display_menu(self):
        print("\nMenu :")
        for section, items in self.menu_items.items():
            print(f"\n{section} :")
            for item in items:
                print(item)


def main():
    menu = Menu()
    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Update Price")
        print("4. Display Menu")
        print("5. Exit")
        choice = input("\nEnter your choice : ")
        if choice == '1':
            name = input("\nEnter item name : ")
            description = input("Enter item description : ")
            price = float(input("Enter item price : "))
            section = input("Enter item section (Press Enter for Miscellaneous) : ").strip() or "Miscellaneous"
            menu.add_item(MenuItem(name, description, price), section)
        elif choice == '2':
            item_name = input("\nEnter the name of the item to remove : ")
            if menu.remove_item(item_name) :
                print(f"{item_name} removed successfully.")
            else :
                print(f"Error : {item_name} not found in the menu.")
        elif choice == '3':
            item_name = input("\nEnter the name of the item to update price : ")
            new_price = float(input("Enter the new price : "))
            if menu.update_price(item_name, new_price) :
                print(f"Price of {item_name} updated successfully.")
            else :
                print(f"Error : {item_name} not found in the menu.")
        elif choice == '4':
            menu.display_menu()
        elif choice == '5':
            print("\nExiting program....\n")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__" :
    print("\n---RESTAURANT PROGRAM---")
    main()
