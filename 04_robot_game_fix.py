# Farming Robot - Harvest Automation System

import random
import time

class FarmMap:
    """Farm map management system - handles wheat placement and map display"""
    
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


class RobotPosition:  
    def __init__(self, x, y, farm_map: FarmMap):
        self.x = x
        self.y = y
        self.farm_map = farm_map
        self.farm_size = farm_map.size
        
    def is_valid(self, x, y):
        return 0 <= x < self.farm_size and 0 <= y < self.farm_size


class PathfindingSystem:
    @staticmethod
    def calculate_distance(x1, y1, x2, y2):

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        print(f"Distance calculation: ({x1},{y1}) -> ({x2},{y2}); Manhattan distance = {dx + dy}")
        return dx + dy
    
    @staticmethod
    def find_nearest_wheat(robot_x, robot_y, farm_map: FarmMap):
        nearest_wheat = None
        min_distance = float('inf')
        
        print(f"Scanning for wheat from position ({robot_x}, {robot_y})...")
        time.sleep(1)
        
        for y in range(farm_map.size):
            for x in range(farm_map.size):
                if farm_map.get_cell(x, y) == 1:  # There's wheat here
                    distance = PathfindingSystem.calculate_distance(robot_x, robot_y, x, y)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_wheat = (x, y)
                        print(f"Found wheat at ({x}, {y}), distance: {distance}")
                        time.sleep(0.5)
        
        if nearest_wheat:
            print(f"Nearest wheat selected: {nearest_wheat} (distance: {min_distance})")
        else:
            print("No wheat found on the map.")
        
        return nearest_wheat


class Robot:
    def __init__(self, name, x, y, farm_map: FarmMap, energy=100):
        self.name = name
        self.position = RobotPosition(x, y, farm_map)
        self.farm_map = farm_map
        self.energy = energy
        self.wheat_collected = 0
        print(f"Robot '{self.name}' initialized at ({x}, {y}) with {energy} energy units.")

    def get_position(self):
        return (self.position.x, self.position.y)
    
    def move_to(self, direction):
        x, y = self.position.x, self.position.y
        valid_directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        
        if direction not in valid_directions:
            print("Invalid direction. Use UP, DOWN, LEFT, or RIGHT.")
            return False
        
        # Calculate new position
        if direction == "UP":
            y -= 1
        elif direction == "DOWN":
            y += 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1

        # Validate and execute movement
        if self.position.is_valid(x, y):
            self.position.x = x
            self.position.y = y
            self.energy -= 1
            print(f"Robot moved {direction} to ({x}, {y}). Energy: {self.energy}")
            time.sleep(1)  # Movement simulation delay
            return True
        else:
            print(f"Cannot move {direction} - would go out of bounds!")
            return False
        
    def harvest(self):
        x, y = self.get_position()
        if self.farm_map.get_cell(x, y) == 1:
            self.farm_map.remove_wheat(x, y)
            self.wheat_collected += 1
            print(f"✓ Harvested wheat at ({x}, {y})! Total collected: {self.wheat_collected}")
            time.sleep(1)  # Harvesting simulation delay
            return True
        else:
            print(f"No wheat to harvest at ({x}, {y}).")
            return False
            
    def get_status(self):
        return f"Robot '{self.name}' - Position: ({self.position.x}, {self.position.y}), Energy: {self.energy}, Wheat: {self.wheat_collected}"


class MovementController:
    @staticmethod
    def move_robot_to_target(robot, target_x, target_y):
        print(f"Moving robot to target position ({target_x}, {target_y})...")
        
        while True:
            robot_x, robot_y = robot.get_position()
            
            # Check if we've reached the target
            if robot_x == target_x and robot_y == target_y:
                print(f"✓ Robot reached target ({target_x}, {target_y})")
                break

            # Prioritize horizontal movement first, then vertical
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
            
            time.sleep(1)  # Movement planning delay


class AutomationSystem:
    @staticmethod
    def patrol_and_harvest(robot):
        print("="*50)
        print("STARTING AUTOMATED HARVEST SYSTEM")
        print("="*50)
        
        print("Initial farm state:")
        robot.farm_map.display(robot.position.x, robot.position.y)
        time.sleep(2)
        
        while robot.energy > 0 and robot.farm_map.count_remaining_wheat() > 0:
            print(f"\n--- Harvest Cycle (Energy: {robot.energy}, Wheat remaining: {robot.farm_map.count_remaining_wheat()}) ---")
            
            # Find nearest wheat
            nearest = PathfindingSystem.find_nearest_wheat(robot.position.x, robot.position.y, robot.farm_map)
            
            if nearest:
                target_x, target_y = nearest
                print(f"Target acquired: ({target_x}, {target_y})")
                
                MovementController.move_robot_to_target(robot, target_x, target_y)
                
                robot.harvest()
                
                # Display updated map
                print("\nUpdated farm state:")
                robot.farm_map.display(robot.position.x, robot.position.y)
                
                print(robot.get_status())
                time.sleep(2)
            else:
                print("No more wheat to harvest.")
                break
        
        # Final summary
        print("\n" + "="*50)
        print("HARVEST MISSION COMPLETE")
        print("="*50)
        print(f"Final Status: {robot.get_status()}")
        print(f"Wheat remaining on farm: {robot.farm_map.count_remaining_wheat()}")


class ManualControlSystem:
    @staticmethod
    def manual_control(robot):
        print("="*50)
        print("MANUAL CONTROL MODE ACTIVATED")
        print("="*50)
        print("Commands: UP, DOWN, LEFT, RIGHT, QUIT")
        
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        
        print("Initial farm state:")
        robot.farm_map.display(robot.position.x, robot.position.y)
        time.sleep(2)
        
        while robot.energy > 0:
            print(f"\n{robot.get_status()}")
            command = input("Enter command: ").strip().upper()
            
            if command == "QUIT":
                print("Exiting manual control mode.")
                break
            elif command in directions:
                # Execute movement
                if robot.move_to(command):
                    # Auto-harvest if wheat is present
                    robot.harvest()
                    
                    # Display updated state
                    print("\nUpdated farm state:")
                    robot.farm_map.display(robot.position.x, robot.position.y)
                    
                    if robot.farm_map.count_remaining_wheat() == 0:
                        print("All wheat harvested! Mission complete!")
                        break
                        
                time.sleep(1)
            else:
                print("Invalid command. Use: UP, DOWN, LEFT, RIGHT, or QUIT")


class GameController:
    @staticmethod
    def choose_control_mode(robot):
        """Main control mode selection interface"""
        print("="*60)
        print("FARMING ROBOT CONTROL SYSTEM")
        print("="*60)
        
        while True:
            print(f"\nCurrent robot status: {robot.get_status()}")
            print(f"Wheat remaining: {robot.farm_map.count_remaining_wheat()}")
            
            if robot.energy <= 0:
                print("\nRobot energy depleted! Mission terminated.")
                break
                
            if robot.farm_map.count_remaining_wheat() == 0:
                print("\nAll wheat harvested! Mission accomplished!")
                break
            
            print("\nAvailable modes:")
            print("AUTO   - Automatic patrol and harvest")
            print("MANUAL - Manual robot control")
            print("QUIT   - Exit system")
            
            mode = input("\nSelect mode: ").strip().upper()
            
            if mode == "AUTO":
                AutomationSystem.patrol_and_harvest(robot)
            elif mode == "MANUAL":
                ManualControlSystem.manual_control(robot)
            elif mode == "QUIT":
                print("Shutting down farming robot system.")
                break
            else:
                print("Invalid selection. Please choose AUTO, MANUAL, or QUIT.")
            
            time.sleep(2)


# ============================================================================
# MAIN EXECUTION PIPELINE
# ============================================================================

def main():
    """Main execution function - entry point of the simulation"""
    print("FARMING ROBOT SIMULATION STARTING")
    time.sleep(2)
    
    # Initialize farm and robot
    print("Initializing farm environment...")
    farm = FarmMap(num_wheat=8)
    time.sleep(1)
    
    print("Deploying farming robot...")
    robot = Robot("HarvestBot-3000", 0, 0, farm, energy=100)
    time.sleep(1)
    
    print("System initialization complete!")
    time.sleep(2)
    
    # Start main control system
    GameController.choose_control_mode(robot)
    
    # Final system shutdown
    print("\n" + "="*60)
    print("FARMING ROBOT SIMULATION TERMINATED")
    print("="*60)
    print("Final Statistics:")
    print(f"  • {robot.get_status()}")
    print(f"  • Wheat remaining on farm: {robot.farm_map.count_remaining_wheat()}")
    print(f"  • Harvest efficiency: {(robot.wheat_collected / farm.total_wheat * 100):.1f}%")


# Execute the simulation
if __name__ == "__main__":
    main()