import random
import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(range(1000))
x = random.choice(arr)

start = time.time()
for i in range(1000):
    linear_search(arr, x)
end = time.time()
print(f"Linear search: {end - start} seconds")

start = time.time()
for i in range(1000):
    binary_search(arr, x)
end = time.time()
print(f"Binary search: {end - start} seconds")