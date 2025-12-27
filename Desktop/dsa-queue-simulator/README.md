Process to Run the Program
To run the simulation, you will need two separate terminal windows (Command Prompts) open at the same time to simulate the Producer-Consumer relationship.

Step 1: Open the Project Directory
Open two Command Prompt windows and navigate to your project folder in both:


cd Desktop\dsa-queue-simulator
Step 2: Start the Traffic Generator (The Producer)
In the first window, run the generator script. This program simulates vehicles arriving at the junction and adding themselves to the queues by writing to the lane files.


python traffic_generator.py
Observation: You will see vehicles like "Car," "Bus," or "Truck" being assigned to Lane A, B, C, or D.

Step 3: Start the Simulator (The Consumer)
In the second window, run the simulator script. This program reads the data, manages the Priority Queue for the lights, and processes the vehicles using FIFO logic.

python simulator.py
Observation: The simulator will display the current Light State (State 1 for Red, State 2 for Green) and show vehicles passing through the junction.

Step 4: Monitoring the Junction
If Lane A (AL2) has more than 5 vehicles, you will see a [!] PRIORITY MODE message.

The simulator will automatically calculate the green light duration based on the formula: T=∣V∣×t.
![2025-12-27 16-28-01](https://github.com/user-attachments/assets/3a7439f1-9338-44a4-8524-43615c07f0ea)



\## 📚 References

\- \*\*Data Structures:\*\* Python `queue` module documentation (\[docs.python.org](https://docs.python.org/3/library/queue.html))

\- \*\*Priority Logic:\*\* "Introduction to Algorithms" (CLRS) - Priority Queue concepts.

\- \*\*IPC Pattern:\*\* File-based Producer-Consumer synchronization patterns.

\- \*\*Traffic Modeling:\*\* Based on the provided Figure 1 Junction Layout.

