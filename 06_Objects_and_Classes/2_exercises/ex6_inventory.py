class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > 0:
            self.__capacity -= 1
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)