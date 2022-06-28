class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
    
    def get_description(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odomter!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_description())

# my_new_car.update_odometer(530)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_description())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size 
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on its current charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print(f"\n===========")
my_tesla.battery.battery_size=100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()