# Base class for vehicles
class Vehicle:
    def __init__(self, name):
        self.name = name  # Public attribute for vehicle name
    
    # Method to be overridden by derived classes for polymorphism
    def move(self):
        pass  # Abstract-like method, implemented by subclasses

# Car class, inherits from Vehicle
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road 🚗"

# Plane class, inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky ✈️"

# Example usage
if __name__ == "__main__":
    car = Car("Sedan")
    plane = Plane("Jet")
    vehicles = [car, plane]  # List to demonstrate polymorphism
    for vehicle in vehicles:
        print(vehicle.move())