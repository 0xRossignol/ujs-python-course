def binary_search(arr: list, target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    mid = (left + right) >> 1
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


# 测试
arr = [1, 13, 26, 33, 45, 55, 68, 72, 83, 99]
index_33 = binary_search(arr, 33, 0, len(arr))
index_58 = binary_search(arr, 58, 0, len(arr))

if index_33 >= 0:
    print(f"关键字33在列表中的索引是：{index_33}")
else:
    print("关键字33不在该列表中")

if index_58 >= 0:
    print(f"关键字58在列表中的索引是：{index_58}")
else:
    print("关键字58不在该列表中")
