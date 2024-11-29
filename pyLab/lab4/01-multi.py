from multiprocessing import Process, Array
import time
import math


# 判断是否为素数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 进程的工作函数
def count_primes(start, end, result, index):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    result[index] = count


if __name__ == "__main__":
    N = 10_000_000
    PROCESSES = 4
    step = N // PROCESSES

    processes = []
    results = Array('i', PROCESSES)  # 用于存储每个进程的结果

    start_time = time.time()

    for i in range(PROCESSES):
        start = i * step
        end = (i + 1) * step if i != PROCESSES - 1 else N
        process = Process(target=count_primes, args=(start, end, results, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_primes = sum(results)
    end_time = time.time()

    print(f"Total primes: {total_primes}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.2f} seconds")
