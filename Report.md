Lab report: Server farms and load balancing
===========================================

> [!NOTE]
> Write your report in this document. You can write it in English or French



Case 1: Base scenario: M/M/1 system
-----------------------------------

Insert the response time plot (mean and 99th percentile) for different utilization levels.

Answer the following questions:

- How does the mean response time change with the load?
- How does the 99th percentile change with the load? 



Case 2: Load balancing with Round-Robin
---------------------------------------

Insert the response time plot (mean and 99th percentile) for different utilization levels.

Asnwer the following questions:

- Is this system a M/M/k system? Explain why.
- How do the mean response time and the 99th percentile change with the load?
- Compare the 99th percentile with the M/M/1 system at a low utilization level (e.g., 10%). What do you observe?
- Compare the 99th percentile with the M/M/1 system at a hight utilization level (e.g., 90%). What do you observe?
- Why is the performance of the load balancing system worse than M/M/1 at low utilization levels?
- Why is the performance of the load balancing system worse tha M/M/1 at high utilization levels?



Case 3: Overdimensioning RR
---------------------------

In case 2 we've simulated a load balancing system where each servers has 1/5 of the capacity of the single server in the M/M/1 system. We've observed that the load balancing system is less efficient.

How many servers are needed, such that the load balancing system has the same 99th percentile response time as the M/M/1 system at 90% utilization?

Show the plot with the response times for this configuration here and interpret the results.

Increasing the number of servers improves the performance of the load balancing system for *high loads*. Is it possible to improve the performance for *low loads* as well?



Case 4: Improving the loadbalancing system
------------------------------------------

The goal of this case is to define a better scheduling algorithm than round-robin. Implement a new scheduling algorithm and evaluate its performance, e.g., at 80% utilization.

Describe the new scheduling algorithm and show the response time plot here. Compare the performance with the round-robin scheduling and with the M/M/1 system.



Conclusion
----------

Document your conclusions here. What did you learn from the simulation results?
