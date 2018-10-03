"""
This function creates an empty array.
Then it starts checking for factors and adds them
so that they are ordered in descending order.
"""
def get_factors(num):
    factors = []
    for i in range(num // 2, 1, -1):
        if(num % i == 0):
            factors.append(i)
    return factors

"""
This function executes get_factors() on a number
and if there are no factors, get_factors() returns an
empty array, which means the number is a prime number.
"""
def isPrime(num):
    if(len(get_factors(num))) == 0:
        return True
    else:
        return False

numCases = int(input().strip())
cases = []

# load test cases
for i in range(numCases):
    cases.append(int(input().strip()))

for case in cases:
    ans = 0
    factors = get_factors(case)

    """
    Since the get_factors() return array is ordered in descending order,
    start going through the array and the first prime number found
    is the largest prime factor.
    """
    for factor in factors:
        if(isPrime(factor)):
            ans = factor
            break
    
    # If no prime factors found, return the number itself.
    if(ans == 0):
        ans = case
    
    print(ans)


