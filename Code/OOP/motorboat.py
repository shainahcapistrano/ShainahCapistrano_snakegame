class Motorboat:


    def __init__(self, max_fuel, current_fuel_level, max_speed, mileage):
        self.max_fuel = max_fuel
        self.current_fuel_level = current_fuel_level
        self.max_speed = max_speed
        self.mileage = mileage

    def add_miles(self, new_miles):
        self.mileage += new_miles

    def update_fuel(self, change_to_fuel):
        self.current_fuel_level += change_to_fuel

    def __str__(self):
        out = "Total Fuel: " + str(self.total_fuel)
        out += "\nCurrent Fuel " + str(self.current_fuel)
        out += "\nMaximum Speed " + str(self.max_speed)
        out += "\nTotal Distance " + str(self.total_mileage)
        return out

def tester():