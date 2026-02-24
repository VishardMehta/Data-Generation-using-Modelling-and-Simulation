import numpy as np
import pandas as pd
from simulation import run_simulation


def generate_dataset(num_samples=1000):
    data = []

    for _ in range(num_samples):
        arrival_rate = np.random.uniform(0.5, 5.0)
        service_rate = np.random.uniform(0.3, 3.0)
        num_counters = np.random.randint(1, 6)

        avg_wait, max_wait, total_served, customers_left = run_simulation(
            arrival_rate, service_rate, num_counters
        )

        overloaded = 1 if avg_wait > 5.0 else 0

        data.append([
            arrival_rate,
            service_rate,
            num_counters,
            avg_wait,
            max_wait,
            total_served,
            customers_left,
            overloaded
        ])

    columns = [
        "arrival_rate",
        "service_rate",
        "num_counters",
        "avg_wait_time",
        "max_wait_time",
        "total_served",
        "customers_left",
        "overloaded"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("../data/queue_dataset.csv", index=False)

    return df
