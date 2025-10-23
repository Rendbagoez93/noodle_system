import time

class WaterSystem:
    def __init__(self):
        self.max_capacity_in_tank = 5000
        self.capacity_in_bucket = 500
        self.current_capacity = 0
        self.current_temp = 25
        
    def open_water_valve(self, seconds):
        water = 0
        flow_rate = 100 # ml per second
        
        while water < seconds:
            self.current_capacity += flow_rate
            self.max_capacity_in_tank -= flow_rate
            water += 1
            time.sleep(1)
            print (f"Filling...{water}s water.") 
            time.sleep(1.5)
            print (f"Current ml in bucket: {self.current_capacity} ml")
        return self.current_capacity
            
    def close_water_valve(self, target_capacity):
        target_capacity = 300
        while self.current_capacity < target_capacity:
            self.current_capacity += 100
        if self.current_capacity == target_capacity:
            print (f"Valve Closed. Current ml in bucket: {self.current_capacity}/{self.capacity_in_bucket} ml in bucket")
        else:
            print ("Error: Overfilled Bucket!")
            
        return self.current_capacity
        
    def heat_up (self, target_temp):
        seconds_needed = 0
        while self.current_temp < target_temp:
            self.current_temp += 5
            seconds_needed += 1
            time.sleep(1.5)
            print (f"Heating... {seconds_needed}s Current Temp: {self.current_temp}°C")

        if target_temp <= 80:
            print ("Water Heated to Target Temperature.")
            time.sleep(1)
            print ("MAINTAINING TEMP...")
        elif target_temp >= 80:
            print ("Warning: High Temperature! Cooling Down...")
        else:
            print ("Low Temperature Detected. Heating Up...")
            
        return seconds_needed

    def empty_bucket(self):
        self.current_capacity = 0
        
    def get_water_status(water_system):
        return f"WaterSystem: {water_system.current_capacity}/{water_system.max_capacity_in_tank} ml in tank"

# water_system = WaterSystem()
# water_system.open_water_valve(3)
# water_system.close_water_valve(300)
# time.sleep(1)
# water_system.heat_up(80)

# print ("=" * 20)

class Dispenser:
    def __init__(self, name, capacity, ml_per_trigger=1):
        self.name = name
        self.capacity = capacity
        self.ml_per_trigger = ml_per_trigger
        self.current_amount = capacity
    
    def trigger(self, times=1):
        amount = times * self.ml_per_trigger
        self.current_amount -= amount
        print (f"Dispensing {amount} ml from {self.name} Dispenser.")
        
    def get_dispenser_status(self):
        return f"{self.name} Current Dispenser: {self.current_amount}/{self.capacity} ml remaining"
    
noodle = Dispenser("Noodle", capacity=50, ml_per_trigger=1)        
ketchup = Dispenser("Ketchup", capacity=1000, ml_per_trigger=1)
sausage = Dispenser("Sausage", capacity=1000, ml_per_trigger=1)
powder = Dispenser("Powder", capacity=1000, ml_per_trigger=1)
    
# noodle.trigger(1)
# print(noodle.get_dispenser_status())
# time.sleep(1)
# ketchup.trigger(3)
# print(ketchup.get_dispenser_status())
# time.sleep(1)
# sausage.trigger(2)
# print(sausage.get_dispenser_status())
# time.sleep(1)
# powder.trigger(3)
# print(powder.get_dispenser_status())
# print ("=" * 20)

class CookingProcess:
    def __init__(self, cooking_time=120, maintain_temp=(75, 80), target_temp=80, Dispenser=Dispenser):
        self.cooking_time = cooking_time  # in seconds
        self.current_temp = target_temp
        self.maintain_temp = maintain_temp
        self.dispenser = Dispenser

    def start_cooking(self):
        print ("Starting Cooking Process...")
        time.sleep(1)
        while self.cooking_time > 0:
            print (f"Cooking... {self.cooking_time}s remaining. Current Temp: {self.current_temp}°C")
            self.cooking_time -= 10
            self.current_temp += 5
            time.sleep(2)
            
    def maintain_temperature(self):
        while self.cooking_time > 0:
            if self.current_temp < self.maintain_temp[0]:
                print ("Heating Up...")
                self.current_temp += 5
            elif self.current_temp > self.maintain_temp[1]:
                print ("Cooling Down...")
                self.current_temp -= 5
            else:
                print ("Maintaining Temperature...")
                
        print ("Cooking Complete!")
        
        return "Dish is ready to be served!"
    
cooking = CookingProcess()
print (cooking.start_cooking())
print (cooking.maintain_temperature())

# class NoodleMachine:
#     def __init__(self):
#         self.water_system = WaterSystem()
#         self.noodle_dispenser = Dispenser("Noodle", capacity=50, ml_per_trigger=1)
#         self.ketchup_dispenser = Dispenser("Ketchup", capacity=1000, ml_per_trigger=1)
#         self.sausage_dispenser = Dispenser("Sausage", capacity=1000, ml_per_trigger=1)
#         self.powder_dispenser = Dispenser("Powder", capacity=1000, ml_per_trigger=1)
#         self.noodle_made = 0
        
#     def make_noodle(self):
#         print ("Filling water...")
#         self.water_system.open_water_valve(3)
#         time.sleep(1)
        
#         print ("Closing water valve...")
#         self.water_system.close_water_valve(300)
#         time.sleep(1)
        
#         print ("Heating water...")
#         self.water_system.heat_up(80)
        
#         time.sleep(1)
#         print ("Dispense Noodle...")
#         self.noodle_dispenser.trigger(1)
#         time.sleep(2)
#         print ("Noodle Dispensed.")
#         time.sleep(2)
        
#         print ("Cooking Noodles...")
#         while self.cooking_time > 0:
#             self.water_system.current_temp += 5
#             self.cooking_time -= 20
#             print (f"Cooking... {self.cooking_time}s remaining. Current Temp: {self.water_system.current_temp}°C")
#             time.sleep(1.5)
#             return self.cooking_time
        
#         if self.cooking_time <= 120:
#             self.water_system.current_temp += 5
#             print (f"Maintaining Heat. Current Temp: {self.water_system.current_temp}°C")
#             return self.water_system.current_temp
        
#         if self.water_system.current_temp > 80:
#             print ("Cooling Down Temperature...")
#         elif self.water_system.current_temp < 80:
#             print ("Heating Up Temperature...")
#         else:
#             print ("Maintaining Temperature...")
        
#         print ("Dispense Seasonings...")
#         self.ketchup_dispenser.trigger(3)
#         time.sleep(1)
#         self.sausage_dispenser.trigger(2)
#         time.sleep(1)
#         self.powder_dispenser.trigger(3)
        
#         print ("Noodles are ready!")
#         self.noodle_made += 1
#         print (f"Total noodles made: {self.noodle_made}")
        
#         print ("Emptying bucket...")
#         self.water_system.empty_bucket()
#         print ("Ready for Next Order!")
        
#     def get_machine_status(self):
#         status = {
#             "Water System": self.water_system.get_water_status(),
#             "Noodle Dispenser": self.noodle_dispenser.get_dispenser_status(),
#             "Ketchup Dispenser": self.ketchup_dispenser.get_dispenser_status(),
#             "Sausage Dispenser": self.sausage_dispenser.get_dispenser_status(),
#             "Powder Dispenser": self.powder_dispenser.get_dispenser_status(),
#         }
#         return status
        
        
# noodle_machine = NoodleMachine()
# print ("Starting Noodle Machine...")
# time.sleep(2)
# noodle_machine.make_noodle()