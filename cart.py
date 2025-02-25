class Cart:
    def __init__(self):
        self.items=[]
        self.total_price=0


    def add_device(self, device, amount):
        if device.stock >= amount:
            self.items.append((device, amount))  # Fix tuple appending
            self.total_price += device.price * amount
            print(f"Added {amount} of {device.name} to the cart.")
        else:
            print(f"Not enough stock for {device.name}. Available: {device.stock}")

    def remove_device(self, device, amount):
        pair = device, amount

    def get_total_price(self):
        return self.total_price
    
    def print_items(self):
        for pair in self.items:
            device = pair[0]
            amount = pair[1]

            print(device, "Amount", amount)
    
    def checkout(self):
        for pair in self.items:
            device = pair[0]
            amount = pair[1]

            if (device.is_available(amount)):
                device.reduce_stock(amount)
                print(device, "Amount", amount)



        print("Total price: ", self.total_price)

