class Robot:
    """Simple robot that moves toward nearest wheat and harvests it."""
    def __init__(self, farm_map, start_x=0, start_y=0):
        self.farm = farm_map
        self.x = start_x
        self.y = start_y
        self.harvested = 0

    def harvest(self):
        if self.farm.remove_wheat(self.x, self.y):
            self.harvested += 1
            print(f"Harvested at ({self.x}, {self.y}) -> total harvested: {self.harvested}")

    def find_nearest_wheat(self):
        nearest = None
        min_dist = None
        for y in range(self.farm.size):
            for x in range(self.farm.size):
                if self.farm.get_cell(x, y) == 1:
                    dist = abs(self.x - x) + abs(self.y - y)
                    if min_dist is None or dist < min_dist:
                        min_dist = dist
                        nearest = (x, y)
        return nearest

    def step_towards(self, tx, ty):
        if tx is None:
            return
        # move one step in x or y toward target
        if self.x < tx:
            self.x += 1
        elif self.x > tx:
            self.x -= 1
        elif self.y < ty:
            self.y += 1
        elif self.y > ty:
            self.y -= 1
        # try to harvest at new position
        self.harvest()
        
        
        
class CookingProcess:   
    def __init__(self, cooking_time):
        self.cooking_time = cooking_time
        self.current_temp = 80
        self.maintain_temp = 80

    def run_with_temparature_control(self):
        elapsed = 0
        print("Starting Cooking Process...")
        while elapsed < self.cooking_time:
            elapsed += 10
            print (f"Cooking... {self.cooking_time - elapsed}s remaining.")
            
            if self.current_temp < self.maintain_temp:
                self.current_temp += 2.5
                print(f"Low Temperature. Heat Up. Current Temp: {self.current_temp}°C")
            elif self.current_temp > self.maintain_temp:
                self.current_temp -= 2.5
                print(f"High Temperature. Cool Down. Current Temp: {self.current_temp}°C")
            else:
                print(f"Stable Temperature. Current Temp: {self.current_temp}°C")
            
            time.sleep(2)
            
        return "Cooking Process Completed."
    
    def run(self):
        elapsed = 0
        print("Starting Cooking Process...")
        while elapsed < self.cooking_time:
            elapsed += 10
            print(f"Cooking... {self.cooking_time - elapsed}s remaining.")
            time.sleep(2)
        return "Cooking Process Completed."
    