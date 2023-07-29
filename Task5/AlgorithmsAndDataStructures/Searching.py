def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
target1 = 5
print(binary_search(arr1, target1))
print(linear_search(arr1, target1))
target2 = 9
print(binary_search(arr1, target2))
print(linear_search(arr1, target2))
