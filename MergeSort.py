import random
import time

cases = [32, 2048, 1048576]
iter = 0

def mergeSort(list: list[int]) -> list[int]:
    if len(list) == 1 or len(list) == 0:
        return list
    listA = mergeSort(list[:len(list)//2])
    listB = mergeSort(list[len(list)//2:])
    list = merge(listA, listB)
    return list

def merge(list1: list[int], list2: list[int]) -> list[int]:
    global iter
    list = []
    while (len(list1) > 0 and len(list2) > 0):
        iter = iter + 1
        if (list1[0] < list2[0]):
            list.append(list1[0])
            list1.pop(0)
       
        elif (list1[0] >= list2[0]):
            list.append(list2[0])
            list2.pop(0)
            
    if (len(list1) > 0):
        list = list + list1
    if (len(list2) > 0):
        list = list + list2
    return list

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
        list = mergeSort(list)
        print("Algorithm execution time:",time.time() - alg_start,"seconds")
        
        print("Number of iterations:", iter)
    
if __name__ == "__main__":
    main()    
