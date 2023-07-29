def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr1 = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr1)
print(arr1)
