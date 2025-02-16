class InventoryCLI:
    def __init__(self):
        self.manager = InventoryManager()

    def run(self):
        while True:
            self._display_menu()
            choice = input("Enter your choice (1-7): ")
            self._handle_choice(choice)

    def _display_menu(self):
        menu = """
        Inventory Management System
        =========================
        1. Add New Item
        2. View All Items
        3. Update Stock
        4. Search Items
        5. Generate Low Stock Report
        6. Delete Item
        7. Exit
        """
        print(menu)

    def _handle_choice(self, choice):
        if choice == "1":
            self._add_item()
        elif choice == "2":
            self._view_all_items()
        elif choice == "3":
            self._update_stock()
        elif choice == "4":
            self._search_items()
        elif choice == "5":
            self._generate_report()
        elif choice == "6":
            self._delete_item()
        elif choice == "7":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def _add_item(self):
        name = input("Enter item name: ")
        description = input("Enter description: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        try:
            item_id = self.manager.add_item(name, description, quantity, price)
            print(f"Item added successfully with ID: {item_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_all_items(self):
        items = self.manager.storage.get_all_items()
        if not items:
            print("No items in inventory.")
            return
        for item in items:
            print(item)

    def _update_stock(self):
        item_id = int(input("Enter item ID: "))
        quantity_change = int(input("Enter quantity change (positive for addition, negative for removal): "))
        if self.manager.update_stock(item_id, quantity_change):
            print("Stock updated successfully")
        else:
            print("Failed to update stock")

    def _search_items(self):
        query = input("Enter search term: ")
        items = self.manager.storage.search_items(query)
        if not items:
            print("No items found.")
            return
        for item in items:
            print(item)

    def _generate_report(self):
        threshold = int(input("Enter low stock threshold: "))
        report = self.manager.generate_low_stock_report(threshold)
        print(report)

    def _delete_item(self):
        item_id = int(input("Enter item ID to delete: "))
        if self.manager.storage.delete_item(item_id):
            print("Item deleted successfully")
        else:
            print("Item not found")
