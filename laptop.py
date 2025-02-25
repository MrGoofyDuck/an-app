from dev import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed
    
    def run_program(self, program_name):
        return f"Running {program_name} on {self.name}..."
    
    def use_keyboard(self):
        return f"Typing on the keyboard of {self.name}..."
    
    def display_info(self):
        return super().display_info() + f", RAM: {self.ram_size}GB, Processor Speed: {self.processor_speed}GHz"
    
    def __str__(self):
        return self.display_info()