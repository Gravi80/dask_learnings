from distributed import Client, LocalCluster, fire_and_forget, as_completed
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


def task(x):
    time.sleep(x)
    print(f"task took: {x} seconds")
    return x


if __name__ == '__main__':
    cluster = LocalCluster()
    client = Client(cluster)  # Pass scheduler IP in case of remote dask cluster
    futures = client.map(task, [1, 5, 10])
    client.gather(futures)  # wait for futures to complete
