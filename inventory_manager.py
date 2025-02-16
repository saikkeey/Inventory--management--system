class InventoryManager:
    def __init__(self):
        self.storage = InventoryStorage()

    def add_item(self, name, description, quantity, price):
        if not name or not description or quantity < 0 or price < 0:
            raise ValueError("Invalid item details")
        return self.storage.add_item(name, description, quantity, price)

    def update_stock(self, item_id, quantity_change):
        item = self.storage.get_item(item_id)
        if not item:
            return False
        new_quantity = item.quantity + quantity_change
        if new_quantity < 0:
            return False
        return self.storage.update_item(item_id, quantity=new_quantity)

    def generate_low_stock_report(self, threshold=5):
        low_stock_items = self.storage.get_low_stock_items(threshold)
        report = "Low Stock Report\n" + "="*20 + "\n"
        for item in low_stock_items:
            report += f"{item.name}: {item.quantity} remaining\n"
        return report
