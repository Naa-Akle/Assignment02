import time
import numpy as np

#a function to define interpolation search
def InterpolationSearch(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]:
        POS = Low + int(((( arr[High] - arr[Low])) * ( target - arr[Low]))/float(High - Low)) '''POS function for interpolation'''

        if arr[POS] == target:
            return POS
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;
    
    return "Not in sequence"
#function to define binary search
def BinarySearch(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]: 
        POS = int((Low + High)/ 2) '''POS formula for binary search'''
        
        if arr[POS] == target:
            return POS
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;
    
    return "Not in sequence"

#function to define sequences 100,1000 and 5000
def main():
  sequence100 = np.random.randint(1,32767, 100)
  sequence1000 = np.random.randint(1,32767, 1000)
  sequence5000 = np.random.randint(1,32767, 5000)

  # Interpolation search for squence 100
  i_start_time_100 = time.perf_counter()
  InterpolationSearch(sequence100, 6)
  i_end_time_100 = time.perf_counter()
  
 # Binary search for squence 100
  b_start_time_100 = time.perf_counter()
  BinarySearch(sequence100, 6)
  b_end_time_100 = time.perf_counter()
  
#function to print time for sequence to complete
  milsec = (i_end_time_100 - i_start_time_100) * 1000
  print("For N = 100, the time taken for interpolation search is %.17f" % milsec)

  milsec1 = (b_end_time_100 - b_start_time_100) * 1000
  print("For N = 100, the time taken for binary search is %.17f" % milsec1 + "\n")

  
  # For sequence 1000
  i_start_time_1000 = time.perf_counter()
  InterpolationSearch(sequence1000, 6)
  i_end_time_1000 = time.perf_counter()

  b_start_time_1000 = time.perf_counter()
  BinarySearch(sequence1000, 6)
  b_end_time_1000 = time.perf_counter()

  milsec = (i_end_time_1000 - i_start_time_1000) * 1000
  print("For N = 1000, the time taken for interpolation search is %.17f" % milsec)

  milsec1 = (b_end_time_1000 - b_start_time_1000) * 1000
  print("For N = 1000, the time taken for binary search is %.17f" % milsec1 + "\n")


  #functions for sequence 5000:
  i_start_time_5000 = time.perf_counter()
  InterpolationSearch(sequence5000, 6)
  i_end_time_5000 = time.perf_counter()

  b_start_time_5000 = time.perf_counter()
  BinarySearch(sequence5000, 6)
  b_end_time_5000 = time.perf_counter()

  milsec = (i_end_time_5000 - i_start_time_5000) * 1000
  print("For N = 5000, the time taken for interpolation search is %.17f" % milsec)

  milsec1 = (b_end_time_5000 - b_start_time_5000) * 1000
  print("For N = 5000, the time taken for binary search is %.17f" % milsec1)
  

if __name__ == "__main__":
    main()