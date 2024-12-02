import threading
import time
import math


# 判断是否为素数的函数
def is_prime(n: int) -> bool:
    # 如果 n 小于 2，直接返回 False（因为素数必须大于 1）
    if n < 2:
        return False
    # 从 2 到 sqrt(n) 进行循环检查，看是否有能整除 n 的数
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 如果找到能整除的数，说明 n 不是素数
    return True  # 如果循环完没有找到，说明 n 是素数


# 线程的工作函数：计算指定区间内的素数个数
def count_primes(start, end, result, index):
    count = 0
    # 遍历从 start 到 end 的每个数，检查是否是素数
    for i in range(start, end):
        if is_prime(i):
            count += 1  # 如果是素数，计数加 1
    # 将当前线程的结果存储在结果列表中
    result[index] = count


if __name__ == "__main__":
    N = 10_000_000  # 上限，计算 1 到 N 之间的素数个数
    THREADS = 8  # 使用的线程数量
    step = N // THREADS  # 每个线程需要计算的区间大小

    threads = []  # 存储线程对象
    results = [0] * THREADS  # 用于存储每个线程计算出的素数个数，初始化为 0

    start_time = time.time()  # 记录开始时间

    # 启动多个线程进行并行计算
    for i in range(THREADS):
        start = i * step  # 当前线程负责的区间起始值
        end = (i + 1) * step if i != THREADS - 1 else N  # 当前线程负责的区间结束值，确保最后一个线程包含 N
        # 创建线程并启动
        thread = threading.Thread(target=count_primes, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 计算所有线程的结果之和，即总的素数个数
    total_primes = sum(results)
    end_time = time.time()  # 记录结束时间

    # 输出结果
    print(f"Total primes: {total_primes}")
    print(f"Time taken with threading: {end_time - start_time:.2f} seconds")
