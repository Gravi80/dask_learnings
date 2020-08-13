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
    print(client)
    super_slow_future = client.submit(super_slow)
    # You can control which worker should execute the task,
    # by passing a list of worker names to submit
    fast_future = client.submit(fast, retries=2, workers=[])
    print(super_slow_future, fast_future)
    print(super_slow_future.result())  # We are also printing the return value
    print("* super_slow_future.result is blocking*")
    print(fast_future.result())
