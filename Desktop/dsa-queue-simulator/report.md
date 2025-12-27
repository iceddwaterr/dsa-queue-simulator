Assignment: Queue-Based Traffic Simulation

Name: Manisha Gurung  

Roll No: 26



 1. Summary of Work

This project simulates a four-way traffic junction (North, South, East, West) using Python. It implements a producer-consumer model where traffic is generated into files and processed by a simulator using Queue and Priority Queue principles.



2. Data Structure Table

| Data Structure | Implementation | Purpose |

| Queue | `queue.Queue` | Manages vehicle flow for lanes A, B, C, and D (FIFO). |

| Priority Logic | `if/else` \& `max()` | Determines which lane gets the Green Light (State 2) based on vehicle count. |

| File Buffer | `.txt` files | Acts as the communication link between programs. |


 3. Junction Logic (Figure 1 \& 2)

 Perspective: Road A (North), B (South), C (East), D (West).

Normal Mode: Average vehicles $|V|$ are served based on the counts in lanes B, C, and D.

Priority Mode (AL2): If Lane A has > 5 vehicles, it is served immediately.

 Conditions: State 2 (Green) is only active for one road at a time to avoid deadlock. State 1 (Red) holds all other queues.

4.  List of Functions (Implementation)

In traffic_generator.py (The Producer)
generate_traffic():

Purpose: Simulates real-time vehicle arrivals.

Logic: Uses a random generator to select a lane (A, B, C, or D) and appends a vehicle ID to the corresponding .txt file.

In simulator.py (The Consumer)
pull_data():

Purpose: Acts as the interface between the file and the Queue.

Logic: Reads each lane's file, Enqueues the data into the Python queue.Queue() structure, and then clears the file to prevent duplicate processing.

calculate_normal_v():

Purpose: Implements the math formula ∣V∣=n1∑∣Li∣.

Logic: Calculates the average number of vehicles in the normal lanes (B, C, and D) to determine how many vehicles should pass during a green light.

run_simulation():

Purpose: The main control loop (The "Brain").

Logic: 1. Checks the size of lane a for the Priority Condition (> 5 vehicles). 2. Assigns State 2 (Green) to the active lane. 3. Performs the Dequeue operation (get()) to remove vehicles from the queue as they "pass" the junction.

 2. Algorithm Analysis (Complexity)

Operation	Function	Time Complexity
Enqueue	put()	O(1)
Dequeue	get()	O(1)
Priority Check	qsize()	O(1)
Average Logic	calculate_normal_v	O(k) where k is number of lanes
Export to Sheets

 3. Final Step: How to update your Report
Type: notepad report.md

Paste the Functions and Complexity sections into the file .

Save and Close.

Push to GitHub:


git add report.md
git commit -m "Doc: Added list of functions and time complexity analysis"
git push origin main


 5. Algorithm & Complexity

1. Poll: Read vehicles from lane files.

2. Evaluate: If Lane A > 5, set as Priority. Else, calculate average v.

3. Transition: Set Active Lane to State 2, others to State 1.

4. Process: Dequeue v vehicles. Time taken = v*t.



Time Complexity: - Enqueue/Dequeue: $O(1)$

 Total Simulation: $O(n)$

