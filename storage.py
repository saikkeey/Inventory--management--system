class InventoryStorage:
    def __init__(self):
        self.items = {}
        self._last_id = 0

    def _generate_id(self):
        self._last_id += 1
        return self._last_id

    def add_item(self, name, description, quantity, price):
        item_id = self._generate_id()
        new_item = Item(item_id, name, description, quantity, price)
        self.items[item_id] = new_item
        return item_id

    def get_item(self, item_id):
        return self.items.get(item_id)

    def update_item(self, item_id, **kwargs):
        if item_id in self.items:
            item = self.items[item_id]
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            return True
        return False

    def delete_item(self, item_id):
        return self.items.pop(item_id, None) is not None

    def get_all_items(self):
        return list(self.items.values())

    def search_items(self, query):
        query = query.lower()
        return [item for item in self.items.values() 
                if query in item.name.lower() or query in item.description.lower()]

    def get_low_stock_items(self, threshold=5):
        return [item for item in self.items.values() if item.quantity <= threshold]
