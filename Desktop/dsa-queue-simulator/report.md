\# Assignment: Queue-Based Traffic Simulation

\*\*Name:\*\* Manisha Gurung  

\*\*Roll No:\*\* 26



\## 1. Summary of Work

This project simulates a four-way traffic junction (North, South, East, West) using Python. It implements a producer-consumer model where traffic is generated into files and processed by a simulator using Queue and Priority Queue principles.



\## 2. Data Structure Table

| Data Structure | Implementation | Purpose |

| :--- | :--- | :--- |

| \*\*Queue\*\* | `queue.Queue` | Manages vehicle flow for lanes A, B, C, and D (FIFO). |

| \*\*Priority Logic\*\* | `if/else` \& `max()` | Determines which lane gets the Green Light (State 2) based on vehicle count. |

| \*\*File Buffer\*\* | `.txt` files | Acts as the communication link between programs. |



\## 3. Junction Logic (Figure 1 \& 2)

\- \*\*Perspective:\*\* Road A (North), B (South), C (East), D (West).

\- \*\*Normal Mode:\*\* Average vehicles $|V|$ are served based on the counts in lanes B, C, and D.

\- \*\*Priority Mode (AL2):\*\* If Lane A has > 5 vehicles, it is served immediately.

\- \*\*Light Conditions:\*\* State 2 (Green) is only active for one road at a time to avoid deadlock. State 1 (Red) holds all other queues.



\## 4. Algorithm \& Complexity

1\. \*\*Poll:\*\* Read vehicles from lane files.

2\. \*\*Evaluate:\*\* If Lane A > 5, set as Priority. Else, calculate average $|V|$.

3\. \*\*Transition:\*\* Set Active Lane to State 2, others to State 1.

4\. \*\*Process:\*\* Dequeue $|V|$ vehicles. Time taken = $|V| \\times t$.



\*\*Time Complexity:\*\* - Enqueue/Dequeue: $O(1)$

\- Total Simulation: $O(n)$

