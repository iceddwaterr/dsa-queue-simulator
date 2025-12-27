import queue
import heapq
import time
import os

class TrafficSimulator:
    def __init__(self):
        # 4.1 Vehicle Queues for North(A), South(B), East(C), West(D)
        self.lanes = {
            'laneA': queue.Queue(),
            'laneB': queue.Queue(),
            'laneC': queue.Queue(),
            'laneD': queue.Queue()
        }
        self.t = 2  # Estimated time to pass one vehicle (T)

    def pull_data(self):
        """Simulates communication via file sharing"""
        for road in ['lanea', 'laneb', 'lanec', 'laned']:
            filename = f"{road}.txt"
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    vehicles = f.readlines()
                for v in vehicles:
                    # Mapping file names to our internal lane keys
                    self.lanes[road.replace('lane', 'lane').capitalize()].put(v.strip())
                open(filename, "w").close() # Clear file after reading

    def calculate_normal_v(self):
        """Formula 3.2: Vehicle Served at once |V| = (1/n) * sum(|Li|)"""
        counts = [self.lanes[l].qsize() for l in ['laneB', 'laneC', 'laneD']]
        n = 3 # Number of normal lanes being averaged
        return sum(counts) // n if n > 0 else 0

    def run_simulation(self):
        print("--- Junction Simulator Active (A:North, B:South, C:East, D:West) ---")
        while True:
            self.pull_data()
            
            # Check Priority Lane AL2 (Section 3.3)
            # If > 5 vehicles, it jumps to State 2 (Green) immediately
            al2_count = self.lanes['laneA'].qsize()
            
            if al2_count > 5:
                active_lane = 'laneA'
                v_to_serve = al2_count # Serve all priority vehicles
                print(f"\n[PRIORITY MODE] Road A (North) has {al2_count} vehicles!")
            else:
                # Normal Condition: Pick the lane with the most traffic
                active_lane = max(self.lanes, key=lambda k: self.lanes[k].qsize())
                v_to_serve = self.calculate_normal_v()
                v_to_serve = max(1, v_to_serve) # Serve at least 1 if queue exists

            if self.lanes[active_lane].empty():
                print("Junction Idle... Waiting for traffic.")
                time.sleep(2)
                continue

            # 3.4 Light Conditions
            # State 2 = Green for active, State 1 = Red for all others
            print(f"\nLIGHT STATE: Road {active_lane[-1]} = STATE 2 (GREEN)")
            print(f"LIGHT STATE: Other Roads = STATE 1 (RED) [Deadlock Avoided]")
            
            # Total Time formula: Green Light Time = |V| * t
            green_time = v_to_serve * self.t
            print(f"Green Light Duration: {green_time} seconds for {v_to_serve} vehicles.")

            for _ in range(v_to_serve):
                if not self.lanes[active_lane].empty():
                    vehicle = self.lanes[active_lane].get()
                    print(f"  >>> {vehicle} passing junction...")
                    time.sleep(self.t)

            print(f"Light Cycle Ended for {active_lane}.")

if __name__ == "__main__":
    sim = TrafficSimulator()
    sim.run_simulation()
# Inside your while loop in simulator.py
print(f"\n--- JUNCTION STATUS ---")
print(f"ROAD D: STATE 2 (GREEN) - Serving {v_to_serve} vehicles")
print(f"ROAD A: STATE 1 (RED)")
print(f"ROAD B: STATE 1 (RED)")
print(f"ROAD C: STATE 1 (RED)")
print(f"-----------------------")