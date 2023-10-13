import random

def merge(start, mid, end, array):
    # Separate the array in two halves
    first_half = [array[i] for i in range(start, mid + 1)]
    second_half = [array[j] for j in range(mid + 1, end + 1)]
    count_1 = 0
    count_2 = 0
    k = start
    # Compare the values in the two arrays and arrange accordingly
    while(count_1 < len(first_half) and count_2 < len(second_half)):
        if first_half[count_1] < second_half[count_2]:
            copy[k] = first_half[count_1]
            count_1 += 1
        else:
            copy[k] = second_half[count_2]
            count_2 += 1
        k += 1

    # To add the remaining elements in the first and second half
    for counter in range(count_1, len(first_half)):
        copy[k] = first_half[counter]
        k += 1
    for counter in range(count_2, len(second_half)):
        copy[k] = second_half[counter]
        k += 1
    # Write the intermediate array back to the original
    for i in range(len(copy)):
        if copy[i] != -1:
            data[i] = copy[i]

# Recursive Algorithm for mergesort
def mergesort(start, end, array):
    if start >= end:
        return
    mid = start + (end - start) // 2 
    mergesort(start, mid, array)
    mergesort(mid + 1, end, array)
    merge(start, mid, end, array)
    
while True:
    try:
        values = int(input("Enter the number of values in array: "))
        break
    except ValueError:
        print("Wrong input entered")

data = []
copy = [- 1 for x in range(values)]
# To make sure that different numbers are used in array 
for count in range(values):
    element = random.randint(0, values * 2)
    while element in data:
        element = random.randint(0, values * 2)
    data.append(element)

print("Before sorting: ")
print(data) 
mergesort(0, values - 1, data)
print("After sorting: ")
print(data)