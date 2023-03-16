import random
import time
import math

cases = [32, 2048, 1048576]
num_it = 0

def maxValueDC(list):
    global num_it
    num_it = num_it + 1
    if (len(list)) == 1 or len(list) == 0:
        return max(list[0], list[len(list)-1])
    else:
        value1 = maxValueDC(list[:len(list)//2])
        value2 = maxValueDC(list[len(list)//2:])
        return max(value1,value2)

def randomList(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, n))
    return list

def main():
    global num_it
    for case in cases:
        print("\nCase:", case)
        ls_start = time.perf_counter()
        list = randomList(case)
        print("List initialization time:",time.perf_counter() - ls_start)
        
        alg_start = time.perf_counter()
        num_it = 0
        value = maxValueDC(list)
        print("Value :",value)
        print ("Number of Iterations: ", num_it)
        print("Algorithm execution time:",time.perf_counter() - alg_start)
    
if __name__ == "__main__":
    main()