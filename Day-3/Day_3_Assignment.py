import numpy as np

# ===================== Section A – Array Creation & Basics =====================

# 1. Take 3 numbers from the user and store them in a NumPy array.
arr1 = np.array([int(x) for x in input("Enter 3 numbers separated by space: ").split()])
print("Array:", arr1)

# 2. Create a 1D array of 5 integers using NumPy. Print its size.
arr2 = np.array([1, 2, 3, 4, 5])
print("Array:", arr2, "Size:", arr2.size)

# 3. Create a 2x3 array filled with zeros.
print("2x3 Zeros:\n", np.zeros((2, 3)))

# 4. Create a 3x2 array filled with ones.
print("3x2 Ones:\n", np.ones((3, 2)))

# 5. Take 2 integers from the user and create an array. Print its shape.
arr3 = np.array([int(x) for x in input("Enter 2 numbers separated by space: ").split()])
print("Array shape:", arr3.shape)

# ===================== Section B – Array Properties =====================

# 1. Create a NumPy array [1,2,3,4]. Print its number of dimensions.
arr4 = np.array([1, 2, 3, 4])
print("Dimensions:", arr4.ndim)

# 2. Take 4 numbers as input, create an array, and print its data type.
arr5 = np.array([int(x) for x in input("Enter 4 numbers: ").split()])
print("Data type:", arr5.dtype)

# 3. Convert an integer array into float type.
print("Converted to float:", arr5.astype(float))

# ===================== Section C – Arithmetic Operations =====================

# 1. create two arrays [1,2,3] and [4,5,6]. Add them element-wise.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", np.add(a, b))

# 2. Multiply two arrays [2,4,6] and [1,3,5]
c = np.array([2, 4, 6])
d = np.array([1, 3, 5])
print("Multiplication:", np.multiply(c, d))

# 3. Divide [10, 20, 30] by [2, 5, 10] 
e = np.array([10, 20, 30])
f = np.array([2, 5, 10])
print("Division:", np.divide(e, f))

# 4. Subtract [5, 10, 15] from [20, 30, 40]
g = np.array([20, 30, 40])
h = np.array([5, 10, 15])
print("Subtraction:", np.subtract(g, h))

#5. Take 2 numbers from the user, put them in an array, and print the square of each.
arr6 = np.array([int(x) for x in input("Enter 2 numbers: ").split()])
print("Squares:", arr6 ** 2)

# ===================== Section D – If-Else with Arrays =====================

# 1. Take 3 marks from user, find average, and check if student passed (>= 40).
marks = np.array([int(x) for x in input("Enter 3 marks: ").split()])
if np.mean(marks) >= 40:
    print("Pass")
else:
    print("Fail")


# 2. Take 3 numbers, find maximum, and check if it is greater than 100.
nums1 = np.array([int(x) for x in input("Enter 3 numbers: ").split()])
if np.max(nums1) > 100:
    print("Max is greater than 100")
else:
    print("Max is not greater than 100")


# 3. Take 5 numbers as input, check if the array size is greater than 4
nums2 = np.array([int(x) for x in input("Enter 5 numbers: ").split()])
if nums2.size > 4:
    print("Array size greater than 4")
else:
    print("Array size not greater than 4")

# 4. Compare averages of two arrays given by user and print which is higher.
arr7 = np.array([int(x) for x in input("Enter numbers for array1: ").split()])
arr8 = np.array([int(x) for x in input("Enter numbers for array2: ").split()])
if np.mean(arr7) > np.mean(arr8):
    print("Array1 has higher average")
else:
    print("Array2 has higher or equal average")

# 5. Create an array of 3 numbers. If the minimum value is less than 0, print “Negative number existsˮ.
arr9 = np.array([int(x) for x in input("Enter 3 numbers: ").split()])
if np.min(arr9) < 0:
    print("Negative number exists")
else:
    print("All numbers are non-negative")

# ===================== Section E – Statistical Functions =====================

# 1. Find the average of [10, 20, 30, 40, 50]
print("Mean:", np.mean([10, 20, 30, 40, 50]))

# 2. Find the median of [7, 2, 9, 1, 6]
print("Median:", np.median([7, 2, 9, 1, 6]))

# 3. Find the standard deviation of [10, 12, 23, 23, 16, 23, 21, 16]
print("Std Dev:", np.std([10, 12, 23, 23, 16, 23, 21, 16]))

# 4. Find the variance of [2, 4, 6, 8, 10]
print("Variance:", np.var([2, 4, 6, 8, 10]))

# 5. Find the maximum salary from [25000, 40000, 35000, 28000]
print("Max Salary:", np.max([25000, 40000, 35000, 28000]))

# 6. Find the minimum temperature from [32, 28, 30, 27, 29]
print("Min Temperature:", np.min([32, 28, 30, 27, 29]))

# ===================== Section F – Small Applications =====================

# 1. Take 3 exam scores from the user. If the average is more than 90, print “Grade Aˮ. Else print “Grade Bˮ.
scores = np.array([int(x) for x in input("Enter 3 exam scores: ").split()])
if np.mean(scores) > 90:
    print("Grade A")
else:
    print("Grade B")

# 2. Ask the user for 2 ages. Find which is larger using NumPy.
ages = np.array([int(x) for x in input("Enter 2 ages: ").split()])
print("Larger age:", np.max(ages))

# 3. Create an array of 3 numbers. If all numbers are even, print “Even arrayˮ. Otherwise, print “Mixedˮ
arr10 = np.array([int(x) for x in input("Enter 3 numbers: ").split()])
if np.all(arr10 % 2 == 0):
    print("Even array")
else:
    print("Mixed")

# 4. Ask the user to enter 2 salaries. Print both and show their difference.
salaries = np.array([int(x) for x in input("Enter 2 salaries: ").split()])
print("Salaries:", salaries, "Difference:", np.subtract(salaries[0], salaries[1]))

# 5. Create an array of [3, 6, 9] . Multiply every element by 10.
arr11 = np.array([3, 6, 9])
print("Multiplied by 10:", arr11 * 10)

# 6. Take 3 floating-point numbers from the user. Convert them into integers using NumPy.
floats = np.array([float(x) for x in input("Enter 3 floating numbers: ").split()])
print("Converted to int:", floats.astype(int))
