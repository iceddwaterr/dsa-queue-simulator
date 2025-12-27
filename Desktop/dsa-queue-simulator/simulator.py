import queue
import time
import os

class TrafficSimulator:
    def __init__(self):
        # 4.1 Vehicle Queues - Keys are exactly 'lanea', 'laneb', etc.
        self.lanes = {
            'lanea': queue.Queue(),
            'laneb': queue.Queue(),
            'lanec': queue.Queue(),
            'laned': queue.Queue()
        }
        self.t = 2  # Time to pass one vehicle (T)

    def pull_data(self):
        """Checks the 4 text files for new vehicles"""
        for road_key in self.lanes.keys():
            filename = f"{road_key}.txt" # lanea.txt, laneb.txt...
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    vehicles = f.readlines()
                for v in vehicles:
                    if v.strip():
                        self.lanes[road_key].put(v.strip())
                # Clear the file after reading so we don't process same cars twice
                open(filename, "w").close()

    def calculate_normal_v(self):
        """Average vehicles in normal lanes (B, C, D)"""
        counts = [self.lanes['laneb'].qsize(), self.lanes['lanec'].qsize(), self.lanes['laned'].qsize()]
        return sum(counts) // 3 if sum(counts) > 0 else 0

    def run_simulation(self):
        print("--- Junction Simulator Active ---")
        print("A=North, B=South, C=East, D=West")
       
        while True:
            self.pull_data()
           
            # 1. Check Priority (Lane A > 5 vehicles)
            al2_count = self.lanes['lanea'].qsize()
           
            if al2_count > 5:
                active_lane = 'lanea'
                v_to_serve = al2_count
                print(f"\n[!] PRIORITY MODE: Road A (North) is congested!")
            else:
                # 2. Normal Mode: Pick the lane with the most waiting cars
                active_lane = max(self.lanes, key=lambda k: self.lanes[k].qsize())
                v_to_serve = self.calculate_normal_v()
                v_to_serve = max(1, v_to_serve) # Serve at least 1

            # If the chosen lane is empty, just wait
            if self.lanes[active_lane].empty():
                time.sleep(1)
                continue

            # 3.4 Display States
            print(f"\n>>> LIGHT CHANGE <<<")
            for road in self.lanes.keys():
                state = "STATE 2 (GREEN)" if road == active_lane else "STATE 1 (RED)"
                print(f"Road {road[-1].upper()}: {state}")

            # Process vehicles
            for _ in range(v_to_serve):
                if not self.lanes[active_lane].empty():
                    vehicle = self.lanes[active_lane].get()
                    print(f"  [Go] {vehicle} passed junction.")
                    time.sleep(self.t)

if __name__ == "__main__":
    sim = TrafficSimulator()
    sim.run_simulation()
