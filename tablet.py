from dev import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight
    
    def browse_internet(self):
        return f"Browsing the internet on {self.name}..."
    
    def use_touchscreen(self):
        return f"Using touchscreen on {self.name}..."
    
    def display_info(self):
        return super().display_info() + f", Screen Resolution: {self.screen_resolution}, Weight: {self.weight}g"
    
    def __str__(self):
        return self.display_info()