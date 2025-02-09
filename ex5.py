import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#1) Linear and Binary Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#2) Mesure Performance

def measure_time(search_func, arr, num_trials=1000, num_iterations=100):
    times = []
    for _ in range(num_trials):
        target = random.choice(arr)
        t = timeit.timeit(lambda: search_func(arr, target), number=num_iterations)
        times.append(t / num_iterations)  
    return np.mean(times)


#3) Plot and Interpolation

def linear_model(x, a, b):
    return a * x + b

def log_model(x, a, b):
    return a * np.log(x) + b

sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linear_times = []
binary_times = []

for size in sizes:
    arr = list(range(size)) 
    linear_times.append(measure_time(linear_search, arr))
    binary_times.append(measure_time(binary_search, arr))


linear_params, _ = curve_fit(linear_model, sizes, linear_times)
binary_params, _ = curve_fit(log_model, sizes, binary_times)


plt.figure(figsize=(10, 5))
plt.plot(sizes, linear_times, 'ro-', label='Linear Search')
plt.plot(sizes, binary_times, 'bo-', label='Binary Search')
plt.plot(sizes, linear_model(np.array(sizes), *linear_params), 'r--', label='Linear Fit')
plt.plot(sizes, log_model(np.array(sizes), *binary_params), 'b--', label='Log Fit')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Search Algorithm Performance')
plt.show()


#4) Discussion 

# Linear search follows an O(n) trend, with parameters: {linear_params}
# Binary search follows an O(log n) trend, with parameters: {binary_params}
# The empirical results align with theoretical complexity expectations.
