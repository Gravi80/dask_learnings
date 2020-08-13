from distributed import Client, LocalCluster, as_completed
import time


def fast():
    time.sleep(1)
    print("fast")
    return "fast"


def slow():
    time.sleep(5)
    print("slow")
    return "slow"


def super_slow():
    time.sleep(10)
    print("super_slow")
    return "super_slow"


if __name__ == '__main__':
    cluster = LocalCluster()
    client = Client(cluster)  # Pass scheduler IP in case of remote dask cluster

    # Dask computes the functions based on the order in which they are received

    # Workers will more likely pick high priority task first
    futures = []
    for i in range(30):
        f3 = client.submit(super_slow, key=f"{super_slow.__name__}{i}")
        futures.append(f3)
        f2 = client.submit(slow, key=f"{slow.__name__}{i}")
        futures.append(f2)
        f1 = client.submit(fast, key=f"{fast.__name__}{i}", priority=10)
        futures.append(f1)

    completed = as_completed(futures)
    # completed is a generator which will return futures as they are completed
    for i in completed:
        i.result()
    # For each future dask generates a key from the function name and
    # if the key of two futures matches it only executes 1 future
