def binary_search_iterative(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) >> 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 测试
arr = [1, 13, 26, 33, 45, 55, 68, 72, 83, 99]
index_33 = binary_search_iterative(arr, 33)
index_58 = binary_search_iterative(arr, 58)

if index_33 >= 0:
    print(f"关键字33在列表中的索引是：{index_33}")
else:
    print("关键字33不在该列表中")

if index_58 >= 0:
    print(f"关键字58在列表中的索引是：{index_58}")
else:
    print("关键字58不在该列表中")
