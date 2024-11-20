"Simulation model for load balancing with SimPy."

import random
from matplotlib import pyplot as plt
import simpy
import numpy as np


# ---------------------------------------------------------------------------
# Request generator
# ---------------------------------------------------------------------------
class Client:
    """A client generates requests and sends them to the load balancer."""
    def generate_requests(self, env, arrival_rate, loadbalancer, num_requests):
        """Generate new requests and send them to the load balancer."""

        for _ in range(num_requests):
            yield env.timeout(random.expovariate(arrival_rate))
            env.process(loadbalancer.handle_request())

# ---------------------------------------------------------------------------
# Load balancer (and server)
# ---------------------------------------------------------------------------
class LoadBalancer:
    """The loadbalancer manages n servers. It can handle requests by forwarding them to the servers."""

    def __init__(self, env, num_servers, service_rate, results):
        self.env = env
        self.servers = [simpy.Resource(env, capacity=1) for _ in range(num_servers)]
        self.service_rate = service_rate
        self.results = results
        self.next_server = 0

    def handle_request(self):
        """Server process: chose a server, put request in queue, wait for service, release resource."""
        arrival_time = self.env.now

        server = self.round_robin()
        job = server.request()
        # Wait for the server to become available (wait in the queue)
        yield job
        # Process the request
        yield self.env.timeout(random.expovariate(self.service_rate))
        departure_time = self.env.now
        self.results.append(departure_time - arrival_time)
        server.release(job)

    # Load balancing policies ----------------------------------------------
    def round_robin(self):
        """Round-robin load balancing policy."""
        server = self.servers[self.next_server]
        self.next_server = (self.next_server + 1) % len(self.servers)
        return server



# ---------------------------------------------------------------------------
# Main functions to run the simulation with different configurations
# ---------------------------------------------------------------------------
def main():
    """Function to run a simulation with a single, but fast, server."""

    response_times_mean = []
    response_times_99 = []

    num_requests = 500_000
    num_servers = 5
    service_rate = 100.0/num_servers
    arrival_rates = list(range(5, 100, 5)) + [99]

    for arrival_rate in arrival_rates:
        print(f"Simulating rho = {arrival_rate/(service_rate*num_servers)}")
        response_times = [] # Used for the simulation results
        env = simpy.Environment()
        load_balancer = LoadBalancer(env, num_servers, service_rate, response_times)
        client = Client()

        env.process(client.generate_requests(env, arrival_rate, load_balancer, num_requests))
        env.run()

        response_times_mean.append(np.mean(response_times))
        response_times_99.append(np.percentile(response_times, 99))

    print(f"Mean response times: {response_times_mean}")
    print(f"99th percentile response times: {response_times_99}")

    rhos = [arrival_rate/(service_rate*num_servers) for arrival_rate in arrival_rates]
    plt.plot(rhos , response_times_mean, label="Mean")
    plt.plot(rhos, response_times_99, label="99th percentile")
    plt.ylim(0, 2.5)
    plt.xlabel("Utilization")
    plt.ylabel("Response time (s)")
    plt.legend()
    plt.savefig("../visualizations/5_servers_rr.png")


# ---------------------------------------------------------------------------
# Run one of the simulation types

main()
