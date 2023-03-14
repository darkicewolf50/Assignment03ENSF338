import requests
import json
import timeit
import matplotlib.pyplot as plt
import random

# URL for array data
array_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json'

# URL for search tasks
tasks_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json'

# Fetch the array data from URL and parse it
response = requests.get(array_url)
array_data = json.loads(response.text)

# Fetch the search tasks from URL and parse it
response = requests.get(tasks_url)
search_tasks = json.loads(response.text)

def binary_search_with_initial_midpoint(arr, x, start, end, initial_midpoint):
    """
    Perform a binary search on the sorted array arr to find the element x.
    
    The initial midpoint for the first iteration is set to initial_midpoint. Successive iterations will just split
    the array in the middle.
    
    Returns the index of x if found, or -1 if x is not in the array.
    """
    if start > end:
        return -1
    
    mid = int(initial_midpoint)
    
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search_with_initial_midpoint(arr, x, start, mid - 1, (start+mid-1) // 2)
    else:
        return binary_search_with_initial_midpoint(arr, x, mid + 1, end, (mid+1+end) // 2)



midpoints = []
times = []

for x in search_tasks:

    # Run the timer for a certain number of loops and repetitions
    initialMidPoint = random.randint(0, len(array_data)-1)
    time = min(timeit.repeat(lambda: binary_search_with_initial_midpoint(array_data, x, 0, (len(array_data)-1), initialMidPoint), setup=lambda: None, number=1000, repeat=5))

    # Calculate the average time per loop
    avg_time = time / 1000

    # Store the midpoint and time for this search task
    midpoints.append(initialMidPoint)
    times.append(avg_time)

# Create a scatterplot of the midpoints and times
plt.scatter(midpoints, times)
plt.xlabel('Initial Midpoint')
plt.ylabel('Average Time per Loop (s)')
plt.title('Binary Search Performance vs. Initial Midpoint')
plt.show()
