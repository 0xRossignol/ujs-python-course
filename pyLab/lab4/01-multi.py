from multiprocessing import Process, Array
import time
import math


# 判断是否为素数的函数
def is_prime(n):
    # 如果 n 小于 2，直接返回 False（因为素数必须大于 1）
    if n < 2:
        return False
    # 从 2 到 sqrt(n) 进行循环检查，看是否有能整除 n 的数
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 如果找到能整除的数，说明 n 不是素数
    return True  # 如果循环完没有找到，说明 n 是素数


# 进程的工作函数：计算指定区间内的素数个数
def count_primes(start, end, result, index):
    count = 0
    # 遍历从 start 到 end 的每个数，检查是否是素数
    for i in range(start, end):
        if is_prime(i):
            count += 1  # 如果是素数，计数加 1
    # 将当前进程的结果存储在共享数组中
    result[index] = count


if __name__ == "__main__":
    N = 10_000_000  # 上限，计算 1 到 N 之间的素数个数
    PROCESSES = 4  # 使用的进程数量
    step = N // PROCESSES  # 每个进程需要计算的区间大小

    processes = []  # 存储进程对象
    results = Array('i', PROCESSES)  # 用于存储每个进程计算出的素数个数，使用共享内存数组

    start_time = time.time()  # 记录开始时间

    # 启动多个进程进行并行计算
    for i in range(PROCESSES):
        start = i * step  # 当前进程负责的区间起始值
        end = (i + 1) * step if i != PROCESSES - 1 else N  # 当前进程负责的区间结束值，确保最后一个进程包含 N
        # 创建进程并启动
        process = Process(target=count_primes, args=(start, end, results, i))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    # 计算所有进程的结果之和，即总的素数个数
    total_primes = sum(results)
    end_time = time.time()  # 记录结束时间

    # 输出结果
    print(f"Total primes: {total_primes}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.2f} seconds")
