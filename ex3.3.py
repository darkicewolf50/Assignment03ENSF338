import sys

arr = []
Size_old = sys.getsizeof(arr)

for i in range(64):
    arr.append(i)
    current_size = sys.getsizeof(arr)
    if(current_size != Size_old):
        print(f"List capacity changed from {Size_old} bytes to {current_size} bytes when adding an element to index {i}")
        Size_old = current_size