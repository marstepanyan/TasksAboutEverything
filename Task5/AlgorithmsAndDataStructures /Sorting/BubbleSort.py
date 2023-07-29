def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Set flag to False to check if any swaps occur in this iteration
        swapped = False

        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swaps occurred, the array is already sorted
        if not swapped:
            break


arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr1)
print(arr1)
