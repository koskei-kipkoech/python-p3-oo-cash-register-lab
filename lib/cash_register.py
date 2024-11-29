#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.item_price = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.item_price.extend([price] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            last_item_price = self.item_price.pop()  
            self.total -= last_item_price
            print(f"The last item '{last_item}' has been voided.")
            if self.items and self.items[-1] == last_item:
                self.void_last_transaction()
        else:
            print("No items to void.")