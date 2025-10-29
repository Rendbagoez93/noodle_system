import time

# Instant Noodles Maker Machine

# Task 1.1

capacity = 500
flow_rate = 100 # per second

def open_water_valve(Seconds):
    total_water = flow_rate * Seconds
    if total_water > capacity:
        total_water = capacity
    return int(total_water)

# print(open_water_valve(5))
# print("=" * 20)

# Task 1.2
temperature = 0 - 100

def is_temperature_ok(current_temp):
    if current_temp >= 75 and current_temp <= 80:
        return True
    else:
        return False

# print(is_temperature_ok(78))
# print(is_temperature_ok(70))
# print("=" * 20)

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
    
# print(add_seasoning(3, 2, 3))
# print(add_seasoning(2, 2, 3))
# print("=" * 20)

# Task 2.1

def fill_bucket(target_amount):
    total_filled = 0
    seconds = 0
    while total_filled < target_amount:
        total_filled += open_water_valve(1)
        seconds += 1
    return seconds

seconds = fill_bucket(600)
# print(f"Need {seconds} seconds to fill the bucket.")
# print("=" * 20)

# Task 2.2

def heat_water(current_temp, target_temp):
    if current_temp >= target_temp:
        return 0
    temp_difference = target_temp - current_temp
    seconds_needed = temp_difference / 5
    return int(seconds_needed)
    
seconds = heat_water(70, 80)
# print(f"Need {seconds} seconds to heat from 70°C to 80°C")
# print("=" * 20)

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

# print(maintain_temp(75, 80))
# print(maintain_temp(85, 77))  
# print(maintain_temp(65, 80))
# print("=" * 20)

# Task 2.4

cooking_time = 120 # in seconds

def cook_noodles(cooking_time):
    if cooking_time >= 120:
        return "READY"
    if cooking_time <= 120:
        return "COOKING"

# print(cook_noodles(130))
# print(cook_noodles(100))
# print("=" * 20)

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

# print(dispense_all_seasonings())
# print ("=" * 20)

# Task 3.1

class WaterSystem:
    def __init__(self):
        self.max_capacity_in_tank = 5000
        self.capacity_in_bucket = 500
        self.current_capacity = 0
        self.current_temp = 25
        
    def open_water_valve(self, seconds):
        water = 0
        flow_rate = 100  # ml per second
        
        while water < seconds:
            # Check if tank has enough water
            if self.max_capacity_in_tank < flow_rate:
                print("Error: Not enough water in tank!")
                break
                
            self.current_capacity += flow_rate
            self.max_capacity_in_tank -= flow_rate
            water += 1
            time.sleep(1)  # Only one sleep call
            print(f"Filling... {water}s. Current ml in bucket: {self.current_capacity} ml")
            
        return self.current_capacity
            
    def close_water_valve(self, target_capacity):
        # Use the parameter instead of hardcoded value
        if target_capacity > self.capacity_in_bucket:
            print(f"Error: Target capacity {target_capacity}ml exceeds bucket capacity {self.capacity_in_bucket}ml!")
            return self.current_capacity
            
        while self.current_capacity < target_capacity:
            if self.max_capacity_in_tank <= 0:
                print("Error: Not enough water in tank!")
                break
            self.current_capacity += 100
            self.max_capacity_in_tank -= 100
            
        if self.current_capacity == target_capacity:
            print(f"Valve Closed. Current ml in bucket: {self.current_capacity}/{self.capacity_in_bucket} ml")
        else:
            print(f"Valve Closed. Current ml in bucket: {self.current_capacity}/{self.capacity_in_bucket} ml")
            
        return self.current_capacity
        
    def heat_up(self, target_temp):
        seconds_needed = 0
        print(f"Heating water from {self.current_temp}°C to {target_temp}°C...")
        while self.current_temp < target_temp:
            self.current_temp += 5
            seconds_needed += 1
            time.sleep(1.5)
            print(f"Heating... {seconds_needed}s Current Temp: {self.current_temp}°C")
            
        return seconds_needed

    def empty_bucket(self):
        print(f"Emptying bucket with {self.current_capacity}ml water")
        self.current_capacity = 0
        
    def get_water_status(self):  # Fixed: removed parameter
        return f"WaterSystem: {self.current_capacity}ml in bucket, {self.max_capacity_in_tank}ml remaining in tank"

class Dispenser:
    def __init__(self, name, capacity, ml_per_trigger=1):
        self.name = name
        self.capacity = capacity
        self.ml_per_trigger = ml_per_trigger
        self.current_amount = capacity
       
    def dispense_noodles(self, times=1):
        for i in range(times):
            if self.current_amount < self.ml_per_trigger:
                print(f"Error: Not enough noodles in {self.name} dispenser! Needed {self.ml_per_trigger} ml for trigger {i+1}, available {self.current_amount} ml")
                return False
            self.current_amount -= self.ml_per_trigger
            print(f"Trigger {i+1}: Dispensed {self.ml_per_trigger} ml from {self.name} Dispenser. Remaining: {self.current_amount} ml")
            time.sleep(1)

    def dispense_ketchup(self, times=1):
        for i in range(times):
            if self.current_amount < self.ml_per_trigger:
                print(f"Error: Not enough ketchup in {self.name} dispenser! Needed {self.ml_per_trigger} ml for trigger {i+1}, available {self.current_amount} ml")
                return False
            self.current_amount -= self.ml_per_trigger
            print(f"Trigger {i+1}: Dispensed {self.ml_per_trigger} ml from {self.name} Dispenser. Remaining: {self.current_amount} ml")
            time.sleep(1)

    def dispense_sausage(self, times=1):
        for i in range(times):
            if self.current_amount < self.ml_per_trigger:
                print(f"Error: Not enough sausage in {self.name} dispenser! Needed {self.ml_per_trigger} ml for trigger {i+1}, available {self.current_amount} ml")
                return False
            self.current_amount -= self.ml_per_trigger
            print(f"Trigger {i+1}: Dispensed {self.ml_per_trigger} ml from {self.name} Dispenser. Remaining: {self.current_amount} ml")
            time.sleep(1)
            
    def dispense_powder(self, times=1):
        for i in range(times):
            if self.current_amount < self.ml_per_trigger:
                print(f"Error: Not enough powder in {self.name} dispenser! Needed {self.ml_per_trigger} ml for trigger {i+1}, available {self.current_amount} ml")
                return False
            self.current_amount -= self.ml_per_trigger
            print(f"Trigger {i+1}: Dispensed {self.ml_per_trigger} ml from {self.name} Dispenser. Remaining: {self.current_amount} ml")
            time.sleep(1)

    def get_dispenser_status(self):
        return f"{self.name}: {self.current_amount}/{self.capacity} ml remaining"

# noodle = Dispenser("Noodle", 500, 1)
# ketchup = Dispenser("Ketchup", 1000, 1)
# sausage = Dispenser("Sausage", 1000, 1)
# powder = Dispenser("Powder", 1000, 1)
# print(noodle.dispense_noodles(1))
# print(ketchup.dispense_ketchup(3))
# print(sausage.dispense_sausage(2))
# print(powder.dispense_powder(3))
# print(noodle.get_dispenser_status())
# print(ketchup.get_dispenser_status())
# print(sausage.get_dispenser_status())
# print(powder.get_dispenser_status())
print("=" * 20)

class CookingProcess:
    def __init__(self, cooking_time, maintain_temp=83, initial_temp=80, min_temp=75, max_temp=90, tolerance=1.5):
        self.cooking_time = cooking_time
        self.current_temp = initial_temp
        self.maintain_temp = maintain_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.tolerance = tolerance

    def run_with_temperature_control(self):  # Fixed type
        elapsed = 0
        print("Starting Cooking Process...")
        while elapsed < self.cooking_time:
            remaining = self.cooking_time - elapsed
            print(f"Cooking... {remaining}s remaining. Current Temp: {self.current_temp}°C")
            elapsed += 10
            self.current_temp += 5
            self.current_temp = max(self.min_temp, min(self.current_temp, self.max_temp))
                      
            if abs(self.current_temp - self.maintain_temp) > self.tolerance:
                print("Checking temperature...")
                if self.current_temp < self.maintain_temp - self.tolerance:
                    self.current_temp += 2.5
                    print(f"Low Temperature. Heat Up. Current Temp: {self.current_temp}°C")
                elif self.current_temp > self.maintain_temp + self.tolerance:
                    self.current_temp -= 5
                    print(f"High Temperature. Cool Down. Current Temp: {self.current_temp}°C")
            else:
                print(f"Stable Temperature (within tolerance). Current Temp: {self.current_temp}°C")
            
            time.sleep(2)
            
        return "Cooking Process Completed."

class NoodleMachine:
    def __init__(self):
        self.water_system = WaterSystem()
        self.cooking_process = CookingProcess(120)
        self.noodle_dispenser = Dispenser("Noodle", capacity=50, ml_per_trigger=1)
        self.ketchup_dispenser = Dispenser("Ketchup", capacity=1000, ml_per_trigger=1)
        self.sausage_dispenser = Dispenser("Sausage", capacity=1000, ml_per_trigger=1)
        self.powder_dispenser = Dispenser("Powder", capacity=1000, ml_per_trigger=1)
        self.noodle_made = 0

    def make_noodle(self):
        print("=" * 50)
        print("Starting noodle preparation...")
        
        print("\n1. Filling water...")
        self.water_system.open_water_valve(3)
        time.sleep(1)

        print("\n2. Closing water valve...")
        self.water_system.close_water_valve(300)  # Now this parameter is actually used
        time.sleep(1)

        print("\n3. Heating water...")
        self.water_system.heat_up(80)
        
        time.sleep(1)
        print("\n4. Dispensing Noodle...")
        (self.noodle_dispenser.dispense_noodles(1))
        (self.noodle_dispenser.get_dispenser_status())

        time.sleep(2)
        print("Noodle Dispensed.")

        print("\n5. Cooking and Maintaining Temperature at 83°C...")
        result = self.cooking_process.run_with_temperature_control()
        print(result)
        time.sleep(1)
                
        print("\n6. Dispensing Seasonings...")
        self.ketchup_dispenser.dispense_ketchup(3)
        (self.ketchup_dispenser.get_dispenser_status())
        
        time.sleep(2)
        self.sausage_dispenser.dispense_sausage(2)
        (self.sausage_dispenser.get_dispenser_status())

        time.sleep(2)
        self.powder_dispenser.dispense_powder(3)
        (self.powder_dispenser.get_dispenser_status())

        time.sleep(2)

        print("\n7. Mixing Noodles...")
        time.sleep(3)
        
        print("Noodles are ready!")
        self.noodle_made += 1
        print(f"Total noodles made: {self.noodle_made}")
        
        print("\n8. Emptying bucket...")
        self.water_system.empty_bucket()
        print("Ready for Next Order!")
        return True
        
    def get_machine_status(self):
        status = {
            "Water System": self.water_system.get_water_status(),
            "Noodle Dispenser": self.noodle_dispenser.get_dispenser_status(),
            "Ketchup Dispenser": self.ketchup_dispenser.get_dispenser_status(),
            "Sausage Dispenser": self.sausage_dispenser.get_dispenser_status(),
            "Powder Dispenser": self.powder_dispenser.get_dispenser_status(),
        }
        return status

if __name__ == "__main__":
    noodle_machine = NoodleMachine()
    print("Starting Noodle Machine...")
    time.sleep(2)
    
    # Initial status
    print("\nInitial Machine Status:")
    for component, status in noodle_machine.get_machine_status().items():
        print(f"  {component}: {status}")
    
    noodle_machine.make_noodle()
    
    # Final status
    print("\nFinal Machine Status:")
    for component, status in noodle_machine.get_machine_status().items():
        print(f"  {component}: {status}")