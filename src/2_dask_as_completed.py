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

    # Collect the results of the futures as they completes
    futures = []
    for i in range(3):
        f1 = client.submit(fast)
        futures.append(f1)
        f1_1 = client.submit(fast, key=f"{fast.__name__}{i}")
        futures.append(f1_1)
        f2 = client.submit(slow)
        futures.append(f2)
        f3 = client.submit(super_slow)
        futures.append(f3)

    completed = as_completed(futures)
    # completed is a generator which will return futures as they are completed
    for i in completed:
        i.result()
    # For each future dask generates a key from the function name and
    # if the key of two futures matches it only executes 1 future
