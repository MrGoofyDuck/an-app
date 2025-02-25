from dev import Device

class Phone(Device):

    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life
    
    def make_call(self):
        return f"Making a call from {self.name}..."
    
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.name}..."
    
    def display_info(self):
        return (Device.display_info(self) +  
                    f", Screen Size: {self.screen_size} inches, "
                    f"Battery Life: {self.battery_life} hours")
    def __str__(self):
        return self.display_info()