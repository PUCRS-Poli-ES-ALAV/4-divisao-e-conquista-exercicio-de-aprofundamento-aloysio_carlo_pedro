import time, random 

cases = [4,8,64]
iter = 0

def multiply(x,y,n):
    global iter
    iter = iter + 1
    if n == 1:
        return x*y
    else:
        m = n//2
        a = x//2**m
        b = x%2**m
        c = y//2**m
        d = y%2**m
        e = multiply(a,c,m)
        f = multiply(b,d,m)
        g = multiply(b,c,m)
        h = multiply(a,d,m)
        return 2**(2*m)*e + 2**m*(g+h) + f
    
def multiply_memoization(x,y,n,cache):
        
    if (x, y, n) in cache:
        return cache[(x, y, n)]

    
    if n == 1:
        result = x * y
    else:
        m = n // 2
        a = x // 2 ** m
        b = x % 2 ** m
        c = y // 2 ** m
        d = y % 2 ** m
        e = multiply_memoization(a, c, m, cache)
        f = multiply_memoization(b, d, m, cache)
        g = multiply_memoization(b, c, m, cache)
        h = multiply_memoization(a, d, m, cache)
        result = 2 ** (2 * m) * e + 2 ** m * (g + h) + f

    # Cache the result for future use
    cache[(x, y, n)] = result

    return result

def generate_random_number(n):
    # Generate a random integer with n bits
    return random.randint(2**(n-1), 2**n-1)

def base_multiply(x,y,i=0):

    res = x%10
    div = x//10
    if div == 0:
        return res*y*10**i
    else:
        return res*y*10**i + base_multiply(div,y,i+1)
    
    
   


def main():
    global iter
    for case in cases:
        iter = 0
        x = generate_random_number(case)
        y = generate_random_number(case)
        start = time.perf_counter()
        print ("\nMultiplication of 2 numbers using Karatsuba's algorithm for", case, "bits: " , multiply(x,y,case))
        end = time.perf_counter()
        print ("Time taken:", end - start)
        print("Number of iterations:", iter)

        print ("Base multiplication of 2 numbers for", case, "bits: " , base_multiply(x,y))
        print ("Time taken:", time.perf_counter() - end)

        start = time.perf_counter()
        print ("Multiplication of 2 numbers using Karatsuba's algorithm with memoization for", case, "bits: " , multiply_memoization(x,y,case,{}))
        end = time.perf_counter()
        print ("Time taken:", end - start)

        
    
if __name__ == "__main__":
    main()
    