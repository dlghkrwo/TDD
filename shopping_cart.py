from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    # able to add item to cart, 
    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    # able to get the size of the cart
    def size(self) -> int:
        return len(self.items)
    
    # able to get the item from the cart
    def get_items(self) -> List[str]:
        return self.items

    #able to get the total price in the cart
    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price
        