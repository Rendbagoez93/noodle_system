import time
import threading


def heat_up(current_temp, target_temp, heating_rate=5):
    while current_temp < target_temp:
        time.sleep(2)
        current_temp += heating_rate
        print(f"Heating... Current Temperature: {current_temp}°C")
    print("Target temperature reached!")
    
def maintain_temperature(current_temp, target_temp, duration=100):
    print("Maintaining temperature...")
    while duration > 0:
        if current_temp < target_temp:
            current_temp += 2  # small heating to maintain temp
        elif current_temp > target_temp:
            current_temp -= 2  # cooling down to maintain temp
        
        duration -= 10
        print(f"Current Temperature: {current_temp}°C, Time left: {duration} seconds")
        time.sleep(2)
    print("Finished maintaining temperature.")
    
def cooking(current_temp, cooking_time=120):
    if current_temp <= 75:
        print("Temperature good for cooking!")
        return
    
    print("Cooking started...")
    while cooking_time > 0:
        cooking_time -= 10
        print(f"Cooking... Time left: {cooking_time} seconds")
        
        time.sleep(2)
    
    print("Cooking completed!")

worker_1 = threading.Thread(target=heat_up, args=(20, 75))
worker_1 = threading.Thread(target=maintain_temperature, args=(75, 75, 100), daemon=True)
worker_2 = threading.Thread(target=cooking, args=(80, 120))

worker_1.start()
worker_1.join()
worker_2.start()


print("All processes completed.")

# # Simulate heating and cooking process using threading
# def main():
#     initial_temp = 20
#     target_temp = 75
#     cooking_temp = 80
#     cooking_duration = 120  # seconds

#     heating_thread = threading.Thread(target=heat_up, args=(initial_temp, target_temp), daemon=True)
#     cooking_thread = threading.Thread(target=cooking, args=(cooking_temp, cooking_duration))

#     heating_thread.start()
#     heating_thread.join()  # Ensure heating is done before cooking starts

#     cooking_thread.start()
#     cooking_thread.join()

#     print("All processes completed.")
    
# cooking_process = main
# print(cooking_process)