import random

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogo_sort(arr):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts

data = [3, 1, 2, 7, 4, 10, 6, 9, 5, 8]
sorted_data, count = bogo_sort(data)
print(f"Sorted: {sorted_data} in {count} attempts")