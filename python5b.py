# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗.")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️.")

# Subclass Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing 🚤.")

# Usage
if __name__ == "__main__":
    vehicles = [
        Car("Sedan"),
        Plane("Boeing 747"),
        Boat("Yacht")
    ]

    for v in vehicles:
        v.move()
