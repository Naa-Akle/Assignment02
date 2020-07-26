'''A program to illustrate the runtime of binary and interpolation search'''

import random
import time
#function to define binary search
def binary_Search(array, target, low, high):
    if low > high:
        return False

    middle = (low + high) // 2
    if array[middle] == target:
        return True

    elif array[middle] > target:

        return binary_Search(array, target, low, middle - 1)
    else:
        return binary_Search(array, target, middle + 1, high)

#function to define interpolation search
def interpolation_Search(array, target, low, high):

    while low <= high and target>= array[low] and target <= array[high]:
        mid = low + ((high - low) / (array[high] - array[low]) * (target - array[low]))
        middle = int(mid)
        if low == high and array[low]==target:
            return True

        elif array[middle] == target:
            return True

        elif array[middle] < target:
            low =middle +1
        else:
            high = middle + 1
    return False

# Running and finding the timing of Binary and interpolation search

#running the program recurrently to allow for different values at each sequence
for i in range(15):
    N = int(input("Enter sequence size,ie.100,1000 or 5000: "))    #allow user to determine N,ie.(100.1000.5000)
    arr = []
    for i in range(N):
        n = random.randint(1, 32768)#getting a random integer between 1 and 32768
        arr.append(n)
    arr.sort()
    print(arr)
    
    target = int(input("Enter your target : "))# input to allow user to enter desired value
    #creating the binary search function
    binary_Search_Start = time.perf_counter()
    status_check=binary_Search(arr, target, 0, len(arr) - 1)
    binary_Search_End = time.perf_counter()
    runtime = (binary_Search_End - binary_Search_Start)*1000  #finding the runtime of binary search in milliseconds
    if status_check:#to check if target is in the sequence
        print("The target is in the sequence")
    else:
        print("The target is not in the sequence")
    print("Time taken by binary search is = ", runtime)
    print("\n")
    
#creating the interpolation search function
    interpolation_Search_Start = time.perf_counter()
    statuscheck=interpolation_Search(arr, target, 0, len(arr) - 1)
    interpolation_Search_End = time.perf_counter()
    runtime2 = (interpolation_Search_End - interpolation_Search_Start)*1000 #finding the runtime of interpolation search in milliseconds
    if statuscheck:
        print("The target is in the sequence")
    else:
        print("The target is not in the sequence")
    print("Time taken by interpolation search is = ", runtime2)
    print("\n")