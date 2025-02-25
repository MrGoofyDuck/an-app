# Device and Phone Management System

## Overview
This project demonstrates a simple management system for electronic devices, specifically focusing on smartphones. It includes classes for `Device` and `Phone`, offering functionalities such as displaying device information, applying discounts, checking stock availability, and more.

## Classes

### Device
The `Device` class represents a general electronic device with the following attributes and methods:

- **Attributes**:
  - `name`: The name of the device.
  - `price`: The price of the device.
  - `stock`: The stock availability of the device.
  - `warranty`: The warranty period of the device.

- **Methods**:
  - `__init__(self, name, price, stock, warranty)`: Initializes a new `Device` instance with the given attributes.
  - `display_info(self)`: Returns a string containing the device's information.
  - `__str__(self)`: Returns a string representation of the device.
  - `apply_discount(self, discount)`: Applies a discount to the device's price.
  - `is_available(self, amount)`: Checks if the specified amount is available in stock.
  - `reduce_stock(self, amount)`: Reduces the stock by the specified amount if available.

### Phone
The `Phone` class inherits from the `Device` class and adds additional attributes and methods specific to smartphones:

- **Attributes**:
  - Inherits all attributes from `Device`.
  - `screen_size`: The screen size of the phone.
  - `battery_life`: The battery life of the phone.

- **Methods**:
  - Inherits all methods from `Device`.
  - `__init__(self, name, price, stock, warranty, screen_size, battery_life)`: Initializes a new `Phone` instance with the given attributes.
  - `make_call(self)`: Simulates making a call from the phone.
  - `install_app(self, app_name)`: Simulates installing an app on the phone.
  - `display_info(self)`: Returns a string containing the phone's information, including the inherited attributes and the phone-specific attributes.

## Example Usage
```python
# Create a new device
device = Device("Generic Device", 100, 50, "1 year")

# Create a new phone
phone = Phone("Smartphone", 300, 30, "2 years", 6.5, 24)

# Display device info
print(device.display_info())

# Display phone info
print(phone.display_info())

# Apply discount to the phone
phone.apply_discount(10)

# Check stock availability
print(phone.is_available(5))

# Reduce stock
phone.reduce_stock(5)

# Make a call
print(phone.make_call())

# Install an app
print(phone.install_app("Weather App"))
