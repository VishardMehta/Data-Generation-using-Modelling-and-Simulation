import simpy
import numpy as np


def customer(env, name, counter, service_rate, wait_times):
    arrival_time = env.now
    with counter.request() as request:
        yield request
        wait = env.now - arrival_time
        wait_times.append(wait)
        service_time = np.random.exponential(1.0 / service_rate)
        yield env.timeout(service_time)


def run_simulation(arrival_rate, service_rate, num_counters, sim_duration=60):
    env = simpy.Environment()
    counter = simpy.Resource(env, capacity=num_counters)
    wait_times = []
    customer_count = [0]

    def customer_generator(env):
        i = 0
        while True:
            yield env.timeout(np.random.exponential(1.0 / arrival_rate))
            i += 1
            env.process(customer(env, f"C{i}", counter, service_rate, wait_times))
            customer_count[0] = i

    env.process(customer_generator(env))
    env.run(until=sim_duration)

    avg_wait = np.mean(wait_times) if wait_times else 0
    max_wait = np.max(wait_times) if wait_times else 0
    total_served = len(wait_times)
    total_arrived = customer_count[0]
    customers_left = total_arrived - total_served

    return avg_wait, max_wait, total_served, customers_left
