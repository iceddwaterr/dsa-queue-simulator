import time
import random

def generate_traffic():
    roads = ['lanea', 'laneb', 'lanec', 'laned']
    print("--- Multi-Lane Traffic Generator Started ---")
    
    while True:
        # Pick a random road to add a vehicle to
        target_road = random.choice(roads)
        with open(f"{target_road}.txt", "a") as f:
            f.write(f"Vehicle_{random.randint(100, 999)}\n")
        
        print(f"Added vehicle to {target_road}")
        # Random arrival time
        time.sleep(random.uniform(0.1, 0.8)) 

if __name__ == "__main__":
    generate_traffic()