import threading
import time
import math


# 判断是否为素数
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 线程的工作函数
def count_primes(start, end, result, index):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    result[index] = count


if __name__ == "__main__":
    N = 10_000_000
    THREADS = 8
    step = N // THREADS

    threads = []
    results = [0] * THREADS  # 用于存储每个线程的结果

    start_time = time.time()

    for i in range(THREADS):
        start = i * step
        end = (i + 1) * step if i != THREADS - 1 else N
        thread = threading.Thread(target=count_primes, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_primes = sum(results)
    end_time = time.time()

    print(f"Total primes: {total_primes}")
    print(f"Time taken with threading: {end_time - start_time:.2f} seconds")
