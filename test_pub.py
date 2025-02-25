from dev import Device
from laptop import Laptop
from smartphone import Phone
from tablet import Tablet
from cart import Cart


devices = [
    Phone("iPhone 15", 999, 10, "1 Year", 6.1, 20),
    Tablet("iPad Pro", 799, 5, "2 Years", "2048x1536", 450),
    Laptop("MacBook Air", 1199, 7, "3 Years", 16, 3.2)
]

cart = Cart()

def show_menu():
    while True:
        print("\n1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            print("\nAvailable Devices:")
            for i, Device in enumerate(devices):
                print(f"{i+1}. {Device.display_info()}")
            
            try:
                device_choice = int(input("Enter device number to add to cart (0 to cancel): "))
                if 1 <= device_choice <= len(devices):
                    amount = int(input("Enter quantity: "))
                    cart.add_device(devices[device_choice - 1], amount)
            except ValueError:
                print("Invalid input.")
        
        elif choice == "2":
            cart.print_items()
            print(f"Total price: ${cart.get_total_price():.2f}")
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select again.")

show_menu()
