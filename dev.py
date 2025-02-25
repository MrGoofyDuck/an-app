class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty


    def display_info(self):
        return (f"Name: {self.name}\n"
                f"Price: {self.price}\n"
                f"Stock: {self.stock}\n"
                f"Warranty Period: {self.warranty}")

    def __str__(self):
        return (f"Name:{self.name},"
                f"Price $:{self.price},"
                f"Stock:{self.stock},"
                f"Warranty Period:{self.warranty}")
    
    def apply_discount(self, discount):
        self.price -= self.price * (discount/100)

    def is_available(self, amount):
        return self.stock >=amount
    
    def reduce_stock (self, amount):
        if self.is_available(amount):
            self.stock -=amount
        else:
            print("Not enough stock available")
        