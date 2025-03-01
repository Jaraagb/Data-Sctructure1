class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel
        self.is_on = False
        self.is_running = False

    def __str__(self):
        return f"Brand: {self.brand}, Fuel: {self.fuel}"

    def start(self):
        if self.fuel <= 10:
            self.is_on = True
            return "Vehicle started with low fuel, please refuel soon"
        elif self.fuel == 0:
            self.is_on = False
            return "Vehicle is off"
        else:
            self.is_on = True
            return "Vehicle started"

    def run(self):
        if self.is_on:
            self.is_running = True
            return "Vehicle is running"
        else:
            return "Vehicle is off"

    def consume_fuel(self):
        while self.fuel > 0:
            self.fuel -= 1
            print(f"Fuel: {self.fuel}")
            if self.fuel == 10:
                self.fuel -= 1
                print("Vehicle with low fuel, please refuel soon")
            elif self.fuel == 0:
                self.is_running = False
                return "Vehicle out of fuel"


vehicle1 = Vehicle("Toyota", 80)
print(vehicle1)

class Motorcycle(Vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand, fuel)
        self.type = "Motorcycle"

    def __str__(self):
        return f"Brand: {self.brand}, Fuel: {self.fuel}, Type: {self.type}"

class Car(Vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand, fuel)
        self.type = "Car"

    def __str__(self):
        return f"Brand: {self.brand}, Fuel: {self.fuel}, Type: {self.type}"

motorcycle1 = Motorcycle("Honda", 20)
print(motorcycle1)
car1 = Car("Chevrolet", 100)
print(car1)
print(motorcycle1.start())
print(motorcycle1.run())
print(motorcycle1.consume_fuel())

