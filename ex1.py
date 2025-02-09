# Exercise 1.3
import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
        
'''
1.  This function calculates a fibonacci sequence through using a recursive function. 
    For any n that is greater than 1, the function calls itself twice - func(n-1) and func(n-2). 
    It adds those values together, and continues to call itself until n = 0 or n = 1.
    In the case where n = 0 or n = 1, the function returns the value of n. This is a base case, which eventually stops the recursion.
    
2.  This is not an example of a divide-and-conquer algorithm. This is because divide and conquer algorithms tend to split the problem into sub-problems, and combines the solutions.
    A divide and conquer algorithm would use memoization or dynamic programming.
    In this case, the fibonacci recursion goes over the sub-problems, as func(n-1) calls func(n-2). This is calculated separately in another branch.
    
3.  The time complexity can be expressed by T(n) = T(n-1) + T(n-2) + O(1). It results in the exponential time complexity O(2^n). Each function call generates two more calls.
    This excludes the base cases (n = 1 and n = 0), therefore the recursive calls have 2^n nodes.
'''

# Exercise 1.4
# 4.

def func2(n, cache):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = func2(n-1, cache) + func2(n-2, cache)
    return cache[n]
    
'''
5. With memoization, intermediate results are saved in a cache for future reuse. In the function, the variable cache is used to store previously computed values in func(n). Redundant recusive calls are prevented, therefore improving performance. Each value of n, is computed only once, hence the expression for the time complexity is O(n).
'''

# 5.
def time_measure(f, n):
    if f == func2:
        return timeit.timeit(lambda: f(n, {}), number=1)
    return timeit.timeit(lambda: f(n), number=1)

n_values = list(range(36))
time_original = [time_measure(func, n) for n in n_values[:30]]
time_memoized = [time_measure(func2, n) for n in n_values]

plt.figure()
plt.plot(n_values[:30], time_original, label="Original Function", marker='o')
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Execution Time of Original Function")
plt.legend()
plt.savefig("ex1.6.1.jpg")
plt.close()

plt.figure()
plt.plot(n_values, time_memoized, label="Memoized Function", marker='o', color='red')
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Execution Time of Memoized Function")
plt.legend()
plt.savefig("ex1.6.2.jpg")
plt.close()


