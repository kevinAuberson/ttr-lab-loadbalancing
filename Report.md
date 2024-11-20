Lab report: Server farms and load balancing
===========================================

> [!NOTE]
> Write your report in this document. You can write it in English or French

Results table
-------------

Fill out the table below to record the simulation results.

Response times (99th percentile) in milliseconds:

| Case                      | 10% utilization | 80% utilization | 90% utilization | 
|---------------------------|----------------:|----------------:|----------------:|
| Case 1: M/M/1             |                 |                 |                 |
| Case 2: 5 servers, RR     |                 |                 |                 |
| Case 3: 7 servers, overd. |                 |                 |                 |
| Case 4: 5 servers, SFQ    |                 |                 |                 |
| Case 4: 5 servers, CQ     |                 |                 |                 |



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



Case 4: Improving the load balancing system
------------------------------------------

Describe the results obtained from the two algorithms (shortest-queue-first and central queue). How do they compare with the round-robin scheduling and with the M/M/1 system?



Case 5: Mixing servers
----------------------

This case considers a mix of a fast and slower server. 

Provide your answers to the questions for the mixed server configuration.

- If you only consider the throughput, which configuration is better: only the fast server, or both servers?
- Can you find a configuration where the response time is better with only the fast server?
- Can you find a configuration where the response time is better with both servers?



Conclusion
----------

Document your conclusions here. What did you learn from the simulation results?
