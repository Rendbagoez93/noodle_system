import time

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
    
    def trigger(self, times=1):
        amount = times * self.ml_per_trigger
        if amount > self.current_amount:
            print(f"Error: Not enough {self.name} in dispenser!")
            return False
        self.current_amount -= amount
        print(f"Dispensing {amount} ml from {self.name} Dispenser.")
        return True
        
    def get_dispenser_status(self):
        return f"{self.name}: {self.current_amount}/{self.capacity} ml remaining"
    
class CookingProcess:   
    def __init__(self, cooking_time, maintain_temp=83, initial_temp=80, min_temp=75, max_temp=90, tolerance=1.5):
        self.cooking_time = cooking_time
        self.current_temp = initial_temp
        self.maintain_temp = maintain_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.tolerance = tolerance

    def run_with_temperature_control(self):  # Fixed typo
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
        if not self.noodle_dispenser.trigger(1):
            print("Failed to dispense noodles!")
            return False
            
        time.sleep(2)
        print("Noodle Dispensed.")

        print("\n5. Cooking and Maintaining Temperature at 83°C...")
        result = self.cooking_process.run_with_temperature_control()
        print(result)
        time.sleep(1)
                
        print("\n6. Dispensing Seasonings...")
        self.ketchup_dispenser.trigger(3)
        time.sleep(1)
        self.sausage_dispenser.trigger(2)
        time.sleep(1)
        self.powder_dispenser.trigger(3)
        time.sleep(1)

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