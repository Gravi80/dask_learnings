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


if __name__ == '__main__':
    cluster = LocalCluster()
    client = Client(cluster)  # Pass scheduler IP in case of remote dask cluster

    print("** If there is no reference to the future then the future will not be executed **")
    client.submit(fast)

    # If you want the task to be executed without caring about the future
    future = client.submit(fast)
    fire_and_forget(future)

    completed = as_completed([future])
    for i in completed:
        i.result()
