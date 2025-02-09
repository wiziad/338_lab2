'''
1) What is a profiler, and what does it do?
A profiler is a tool that analyzes a program’s performance by tracking function calls, execution time, and resource usage. 
It helps identify bottlenecks, showing which parts of the code take the most time or are called the most frequently.

2) How does profiling differ from benchmarking?
Profiling gives a detailed breakdown of execution time per function, showing where time is spent inside the code. 
Benchmarking, on the other hand, just measures overall execution time without giving insights into specific functions.
Profiling helps with optimization, while benchmarking is more about performance comparison

'''



import timeit

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    #return [i**2 for i in range(100000000)]
    return (i**2 for i in range(10000000)) 




#3) Use a profiler to measure execution time of the program

import cProfile

cProfile.run("test_function()")
#cProfile.run("third_function()")
cProfile.run("sum(third_function())") 

'''
4) Discuss a sample output. Where does execution time go?

Output: 

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    55/10    0.000    0.000    0.000    0.000 ex3.py:16(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:23(test_function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 7.489 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.719    0.719    7.489    7.489 <string>:1(<module>)
        1    6.770    6.770    6.770    6.770 ex3.py:29(third_function)
        1    0.000    0.000    7.489    7.489 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Answer:        

The profiling output shows that test_function() and its recursive sub_function() execute quickly, with sub_function() making 55 total calls (including recursive ones) 
but consuming negligible time. In contrast, third_function() is the main bottleneck, taking 6.77 seconds out of the 7.49-second total runtime. This happens because it 
creates a massive list of 10 million squared numbers, which is both computationally and memory-intensive. A possible optimization would be using a generator 
((i**2 for i in range(10000000))), which would generate values on demand instead of storing them all in memory, reducing execution time and memory usage.

'''