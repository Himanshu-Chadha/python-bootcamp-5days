
import numpy as np

arr = np.array([3, 8, 1, 6, 0, 7])
count_greater_4 = np.sum(arr > 4)
print("Array:", arr)
print("Count of elements > 4:", int(count_greater_4))
