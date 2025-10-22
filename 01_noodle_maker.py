# Instant Noodles Maker Machine

# Task 1.1

capacity = 500
flow_rate = 100 # per second

def open_water_valve(Seconds):
    total_water = flow_rate * Seconds
    if total_water > capacity:
        total_water = capacity
    return int(total_water)

print(open_water_valve(5))
print("=" * 20)

# Task 1.2
temperature = 0 - 100

def is_temperature_ok(current_temp):
    if current_temp >= 75 and current_temp <= 80:
        return True
    else:
        return False

print(is_temperature_ok(78))
print(is_temperature_ok(70))
print("=" * 20)

# Task 1.3

ketchup = 1 # ml per trigger
sausage = 1
powder = 1

# Recipe
right_ketchup = 3
right_sausage = 2
right_powder = 3

def add_seasoning(ketchup_ml, sausage_ml, powder_ml):
    if ketchup_ml == right_ketchup and sausage_ml == right_sausage and powder_ml == right_powder:
        return True
    else:
        return False
    
print(add_seasoning(3, 2, 3))
print(add_seasoning(2, 2, 3))
print("=" * 20)

# Task 2.1

def fill_bucket(target_amount):
    total_filled = 0
    seconds = 0
    while total_filled < target_amount:
        total_filled += open_water_valve(1)
        seconds += 1
    return seconds

seconds = fill_bucket(600)
print(f"Need {seconds} seconds to fill the bucket.")
print("=" * 20)

# Task 2.2

def heat_water(current_temp, target_temp):
    if current_temp >= target_temp:
        return 0
    temp_difference = target_temp - current_temp
    seconds_needed = temp_difference / 5
    return int(seconds_needed)
    
seconds = heat_water(70, 80)
print(f"Need {seconds} seconds to heat from 70°C to 80°C")
print("=" * 20)

# Task 2.3

min_temp = 75
max_temp = 80

def maintain_temp(current_temp, target_temp):
    if current_temp < min_temp:
        return "INCREASE"
    elif current_temp > max_temp:
        return "DECREASE"
    else:
        return "MAINTAIN"

print(maintain_temp(75, 80))
print(maintain_temp(85, 77))  
print(maintain_temp(65, 80))
print("=" * 20)

# Task 2.4

cooking_time = 120 # in seconds

def cook_noodles(cooking_time):
    if cooking_time >= 120:
        return "READY"
    if cooking_time <= 120:
        return "COOKING"

print(cook_noodles(130))
print(cook_noodles(100))
print("=" * 20)

# Task 2.5

ketchup = 1 # ml per trigger
sausage = 1
powder = 1

def dispense_all_seasonings():
    right_ketchup = 3 * ketchup
    right_sausage = 2 * sausage
    right_powder = 3 * powder
    
    result = {
        "ketchup" : right_ketchup, 
        "sausage" : right_sausage, 
        "powder" : right_powder
    }
    return result 

print(dispense_all_seasonings())
print ("=" * 20)

# Task 3.1

class WaterSystem:
    def __init__(self):
        self.max_capacity_in_tank = 5000
        self.capacity_in_bucket = 500
        self.current_capacity = 0
        self.current_temp = 25
        self.is_valve_open = False
        
    def open_water_valve(self, seconds):
        flow_rate = 100 # ml per second
        water = seconds * flow_rate 
        self.current_capacity += water
        self.max_capacity_in_tank -= water
    
    def close_water_valve(self):
        if self.capacity_in_bucket > 0:
            self.capacity_in_bucket = 500
        else:
            self.capacity_in_bucket = 0
        
    def heat_up (self, target_temp):
        seconds_needed = 0
        while self.current_temp < target_temp:
            self.current_temp += 5
            seconds_needed += 1
        return seconds_needed
    
    def empty_bucket(self):
        self.current_capacity = 0
        
    def get_water_status(water_system):
        return f"WaterSystem: {water_system.current_capacity}/{water_system.max_capacity_in_tank} ml in tank"

water_system = WaterSystem()
water_system.open_water_valve(3)
print(water_system.current_capacity)
print(water_system.get_water_status())

print ("=" * 20)

class Dispenser:
    def __init__(self, name, capacity, ml_per_trigger=1):
        self.name = name
        self.capacity = capacity
        self.ml_per_trigger = ml_per_trigger
        self.current_amount = capacity
    
    def trigger(self, times=1):
        amount = times * self.ml_per_trigger
        self.current_amount -= amount
        
    def get_dispenser_status(self):
        return f"{self.name} Current Dispenser: {self.current_amount}/{self.capacity} ml remaining"
    
noodle = Dispenser("Noodle", capacity=50, ml_per_trigger=1)        
ketchup = Dispenser("Ketchup", capacity=1000, ml_per_trigger=1)
sausage = Dispenser("Sausage", capacity=1000, ml_per_trigger=1)
powder = Dispenser("Powder", capacity=1000, ml_per_trigger=2)
    
noodle.trigger(1)
print(noodle.get_dispenser_status())

ketchup.trigger(3)
print(ketchup.get_dispenser_status())

sausage.trigger(2)
print(sausage.get_dispenser_status())

powder.trigger(3)
print(powder.get_dispenser_status())
print ("=" * 20)

class NoodleMachine:
    def __init__(self):
        self.water_system = WaterSystem()
        self.noodle_dispenser = Dispenser("Noodle", capacity=50, ml_per_trigger=1)
        self.ketchup_dispenser = Dispenser("Ketchup", capacity=1000, ml_per_trigger=1)
        self.sausage_dispenser = Dispenser("Sausage", capacity=1000, ml_per_trigger=1)
        self.powder_dispenser = Dispenser("Powder", capacity=1000, ml_per_trigger=1)
        self.cooking_time = 120
        self.noodle_made = 0
        
    def make_noodle(self):
        print ("Filling water...")
        self.water_system.open_water_valve(3)
        
        print ("Heating water...")
        self.water_system.heat_up(11)
        
        print ("Dispense Noodle...")
        self.noodle_dispenser.trigger(1)
        
        print ("Dispense Seasonings...")
        self.ketchup_dispenser.trigger(3)
        self.sausage_dispenser.trigger(2)
        self.powder_dispenser.trigger(3)
        
        print ("Cooking Noodles...")
        for second in range(self.cooking_time):
            pass
        
        print ("Noodles are ready!")
        self.noodle_made += 1
        print (f"Total noodles made: {self.noodle_made}")
        
        print ("Emptying bucket...")
        self.water_system.empty_bucket()
        print ("Ready for Next Order!")
        
    def get_machine_status(self):
        status = {
            "Water System": self.water_system.get_water_status(),
            "Noodle Dispenser": self.noodle_dispenser.get_dispenser_status(),
            "Ketchup Dispenser": self.ketchup_dispenser.get_dispenser_status(),
            "Sausage Dispenser": self.sausage_dispenser.get_dispenser_status(),
            "Powder Dispenser": self.powder_dispenser.get_dispenser_status(),
        }
        return status
        
noodle_machine = NoodleMachine()

print("NOODLE_MAKER_MACHINE")
print ("=" * 20)

print("INITIAL MACHINE STATUS")
for key, value in noodle_machine.get_machine_status().items():
        print(f"{key}: {value}")
print ("=" * 20)

print("MAKING NOODLE #1...")
print("="*20)
noodle_machine.make_noodle()
print("="*20)

print("\n" + "="*20)
print("MAKING NOODLE #2...")
print("="*20)
noodle_machine.make_noodle()
print("="*20)

print("FINAL MACHINE STATUS")
for key, value in noodle_machine.get_machine_status().items():
    print(f"{key}: {value}")
print("=" * 20)

