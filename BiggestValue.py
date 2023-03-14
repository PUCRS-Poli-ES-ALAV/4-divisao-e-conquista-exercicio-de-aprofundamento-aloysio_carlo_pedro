import random
import time

cases = [32, 2048, 1048576]
iter = 0

def biggestValue(list):
    global iter
    biggest = list[0]
    for i in range(len(list)):
        iter = iter + 1
        if list[i] > biggest:
            biggest = list[i]
    return biggest

def randomList(n):
    list = []
    for _ in range(n):
        list.append(random.randint(0, n))
    return list

def main():
    global iter
    for case in cases:
        iter = 0
        print("\nCase:", case)
        ls_start = time.time()
        list = randomList(case)
        print("List initialization time:",time.time() - ls_start,"seconds")
        
        alg_start = time.time()
        list = biggestValue(list)
        print("Algorithm execution time:",time.time() - alg_start,"seconds")
        
        print("Number of iterations:", iter)
    
if __name__ == "__main__":
    main()
    