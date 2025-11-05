# Farming Robot - Harvest Automation

import random
import time

class FarmMap:
    """This class is ALREADY DONE - just copy and use it!"""
    
    def __init__(self, num_wheat=10):
        self.size = 9
        self.map = self._create_map()
        self.total_wheat = num_wheat
        self._place_wheat(num_wheat)
    
    def _create_map(self):
        """Creates a 9x9 grid filled with 0"""
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def _place_wheat(self, num_wheat):
        """Randomly places wheat on the map"""
        placed = 0
        while placed < num_wheat:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.map[y][x] == 0:  # Empty cell
                self.map[y][x] = 1  # Place wheat
                placed += 1
    
    def get_cell(self, x, y):
        """Returns what's at position (x, y): 0=empty, 1=wheat"""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.map[y][x]
        return -1  # Out of bounds
    
    def remove_wheat(self, x, y):
        """Removes wheat from position (x, y)"""
        if self.map[y][x] == 1:
            self.map[y][x] = 0
            return True
        return False
    
    def count_remaining_wheat(self):
        """Counts how many wheat are left on map"""
        count = 0
        for row in self.map:
            count += sum(row)
        return count
    
    def display(self, robot_x, robot_y):
        """Displays the map with robot position"""
        print("\n    ", end="")
        for i in range(self.size):
            print(f"{i:3}", end=" ")
        print()
        
        for y in range(self.size):
            print(f"{y} ", end="")
            for x in range(self.size):
                if x == robot_x and y == robot_y:
                    print("[ R ]", end="")
                elif self.map[y][x] == 1:
                    print("[ W ]", end="")
                else:
                    print("[ . ]", end="")
            print()
        print()

# map = FarmMap(num_wheat=10)
# print (map.display(0, 0))

print ("=" * 20)

class RobotPosition:
    def __init__ (self, x, y, farm_map: FarmMap):
        self.x = x
        self.y = y
        self.farm_map = farm_map
        self.farm_size = farm_map.size
        
    def is_valid(self, x, y):
        if 0 <= x < self.farm_size and 0 <= y < self.farm_size:
            return True
        else:
            return False
            
# print(RobotPosition(0, 0, map).is_valid(5, 8))
# print(RobotPosition(0, 0, map).is_valid(0, -1))


# Calculating Distance
def calculate_distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    print(f"calculate_distance called with: ({x1},{y1}) -> ({x2},{y2}); dx={dx}, dy={dy}")
    return dx + dy

time.sleep(2)

# distance = calculate_distance(3, 2, 5, 4)
# print(distance)  


def find_nearest_wheat(robot_x, robot_y, farm_map: FarmMap):
    nearest_wheat = None
    min_distance = float('inf')
    for y in range(farm_map.size):
        for x in range(farm_map.size):
            if farm_map.get_cell(x, y) == 1:  # There's wheat here
                distance = calculate_distance(robot_x, robot_y, x, y)
                if distance < min_distance:
                    min_distance = distance
                    nearest_wheat = (x, y)
                    time.sleep(2)
    return nearest_wheat

def loop_finding_wheat(robot_x, robot_y, farm_map: FarmMap):
    while farm_map.count_remaining_wheat() > 0:
        nearest = find_nearest_wheat(robot_x, robot_y, farm_map)
        if nearest:
            print(f"Nearest wheat at: {nearest}")
            robot_x, robot_y = nearest
            farm_map.remove_wheat(robot_x, robot_y)
            farm_map.display(robot_x, robot_y)
        else:
            print("No more wheat found.")
            break

# farm = FarmMap(num_wheat=15)
# near = find_nearest_wheat(4, 4, farm)
# print("Nearest wheat at:", near)
# print("Loop finding wheat:")
# loop_finding_wheat(4, 8, farm)



# Robot Class

class Robot:
    def __init__ (self, robot, x, y, farm_map: FarmMap, energy=100):
        self.robot = robot
        self.position = RobotPosition(x, y, farm_map)
        self.farm_map = farm_map
        self.energy = energy
        self.wheat_collected = 0

    def get_position(self):
        return (self.position.x, self.position.y)
    
    def move_to(self, direction):
        x, y = self.position.x, self.position.y
        valid_directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        if direction not in valid_directions:
            print("Invalid direction. Use UP, DOWN, LEFT, or RIGHT.")
            return False
        
        if direction == "UP":
            y -= 1
        elif direction == "DOWN":
            y += 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1

        if self.position.is_valid(x, y):
            self.position.x = x
            self.position.y = y
            self.energy -= 1
            print(f"Moved {direction} to ({x}, {y}). Energy left: {self.energy}. Now at: ({self.position.x}, {self.position.y})")
            return True
        else:
            print(f"Cannot move {direction} from ({self.position.x}, {self.position.y}) - would go out of bounds!")
            return False
        
  
    def harvest(self):
        x, y = self.get_position()
        if self.farm_map.get_cell(x, y) == 1:
            self.farm_map.remove_wheat(x, y)
            self.wheat_collected += 1
            print(f"Harvested wheat at ({x}, {y}). Total wheat collected: {self.wheat_collected}")
            return True
        else:
            print(f"No wheat to harvest at ({x}, {y}).")
            return False
            
    def get_status(self):
        return f"Robot Position: ({self.position.x}, {self.position.y}), Energy: {self.energy}, Wheat Collected: {self.wheat_collected}"
    pass

# farm = FarmMap(num_wheat=5)
# robot = Robot("Robo", 0, 0, farm)

# print(robot.get_status())
# print(robot.get_position())  # Should be (0, 0)

# robot.move_to("RIGHT")
# print(robot.get_position())  
# print(robot.energy)          # Should be 99

# robot.move_to("DOWN")
# robot.move_to("DOWN")
# robot.move_to("DOWN")
# robot.move_to("DOWN")
# print(robot.get_position())  

# result = robot.harvest()      
# print("Harvest result:", result)

# Task 3:

def move_robot_to_wheat(robot, target_x, target_y):
    while True:
        robot_x, robot_y = robot.get_position()
        
        if robot_x == target_x and robot_y == target_y:
            break

        if robot_x < target_x:
            if not robot.move_to("RIGHT"):
                break
            
        elif robot_x > target_x:
            if not robot.move_to("LEFT"):
                break
            
        elif robot_y < target_y:
            if not robot.move_to("DOWN"):
                break
            
        elif robot_y > target_y:
            if not robot.move_to("UP"):
                break
            
        time.sleep(2)
        
farm = FarmMap(num_wheat=6)
robot = Robot("Robo", 0, 0, farm)

# move_robot_to_wheat(robot, 4, 6)
# print(robot.get_position())  # Should be (4, 6)
# print(robot.energy)          # Should be 92 (8 moves)

def patrol_and_harvest(robot):
    
    print("Initial Map State:")
    robot.farm_map.display(robot.position.x, robot.position.y)
    
    while robot.energy > 0 and robot.farm_map.count_remaining_wheat() > 0:
        nearest = find_nearest_wheat(robot.position.x, robot.position.y, robot.farm_map)
        if nearest:
            target_x, target_y = nearest
            move_robot_to_wheat(robot, target_x, target_y)
            robot.harvest()
        else:
            print("No more wheat to harvest.")
            break
        
        print("\nCurrent Map State:")
        robot.farm_map.display(robot.position.x, robot.position.y)

farm = FarmMap(num_wheat=6)
robot = Robot("Robo", 0, 0, farm)

print (patrol_and_harvest(robot))

# Adding Manual Controls

def manual_control(robot):
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    print("Initial Map State:")
    robot.farm_map.display(robot.position.x, robot.position.y)
    
    while robot.energy > 0:
        command = input("Enter move direction (UP, DOWN, LEFT, RIGHT) or QUIT to exit: ").strip().upper()
        if command == "QUIT":
            print("Exiting manual control.")
            break
        elif command in directions:
            robot.move_to(command)
            robot.harvest()
            print(robot.get_status())
            
            # Display updated map after each move
            print("\nCurrent Map State:")
            robot.farm_map.display(robot.position.x, robot.position.y)
            
        else:
            print("Invalid command. Please enter UP, DOWN, LEFT, RIGHT, or QUIT.")
            
    
# manual = Robot("ManualBot", 0, 0, farm)

# print("Starting Manual Control. Type QUIT to exit.")
# print(manual_control(manual))
# print(manual.get_status())

def choosing_control_mode(robot):
    while True:
        mode = input("Choose control mode: AUTO or MANUAL (or QUIT to exit): ").strip().upper()
        if mode == "AUTO":
            print("Starting Automatic Patrol and Harvest...")
            patrol_and_harvest(robot)
        elif mode == "MANUAL":
            print("Starting Manual Control...")
            manual_control(robot)
        elif mode == "QUIT":
            print("Exiting control mode selection.")
            break
        else:
            print("Invalid choice. Please enter AUTO, MANUAL, or QUIT.")

print("=" * 50)

