def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
