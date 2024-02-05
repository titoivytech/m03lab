#jose solis
#02/04/2024
#m03lab
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

        # Get user input
vehicle_type = input("Enter the vehicle type (car, truck, plane, boat: ")
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an instance of Automobile with user input
user_car = Automobile(vehicle_type=vehicle_type, year=year, make=make, model=model, doors=doors, roof=roof)

# Output the information
print("\nVehicle Information:")
print(f"  Vehicle type: {user_car.vehicle_type}")
print(f"  Year: {user_car.year}")
print(f"  Make: {user_car.make}")
print(f"  Model: {user_car.model}")
print(f"  Number of doors: {user_car.doors}")
print(f"  Type of roof: {user_car.roof}")