Server farms and load balancing
===============================

The goal of this lab is to simulate a server farm with a load balancer. In particular, we will evaluate the questions:

- What is better: a single fast server or several slower servers?
- How does the scheduling algorithm (round-robin, random, shortest queue first) affect the performance of the system?

This lab only considers markovian traffic, i.e., the arrival and service times are exponentially distributed. In a follow-up lab, we will consider non-markovian traffic.

> [!NOTE]
> Write your report using the template `Report.md`. You can write it in English or French



Case 1: Base scenario: M/M/1 system
-----------------------------------

As a baseline for comparison, we will first simulate a single fast server system with an M/M/1 queue.

In the `./models/` directory, you will find a Python script that simulates an M/M/1 system.

- The server has an exponential service with rate $\mu = 100$ requests per second
- The arrival rate of requests is between $\lambda = 5..99$ requests per second (5 - 99% utilization)
- The simulation script computes and plots the mean response time and the 99th percentile of the response time for file requests

Run this model to create the plot.

Interpret the results following the template in the `Report.md` file.



Case 2: Load balancing with Round-Robin
---------------------------------------

In this step we want to compare Case 1 (single fast server) with a load balancing configuration with 5 slow servers and round-robin scheduling.

Slighly modify the simulation script to simulate a system with 5 servers, each with a service rate of $\mu = 20$ requests per second. The request generator should use round-robin scheduling to assign requests to the servers.

Interpret the results following the template in the `Report.md` file.



Case 3: Overdimensioning RR
---------------------------

In Case 2 we've observed that loadbalancing with round-robin is inefficient. But how inefficient is it really? We want to quantify this. Or formulated differenty: how many servers do we need to achieve the same performance as a single fast server?

Write down the 99th percentile of the response time for the M/M/1 system at 90% utilization. This is the target value.

Now, modify the simulation script:

- keep the service rate of the servers at $\mu = 20$ requests per second, i.e., the same as in Case 2
- run the simulation with 6, 7, ... servers until you find a configuration where the 99th percentile of the response time at 90% utilization is equal or below the target value.

This should improve the performance of the loadbalancing system for high loads.
Is it possible to improve the performance for low loads as well?


Case 4: Improving the load balancing system
-------------------------------------------

Round-robin is inefficient and much less efficient than a true M/M/k system would be. Can we improve the performance of the loadbalancing system?

The goal of this case is to define a better scheduling algorithm than round-robin. 

To do this, implement a better scheduling algorithm. Then evaluate its performance and compare it to previous results, e.g., at 80% utilization.
