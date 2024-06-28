class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def divide_until_fail(number, divisor):
            while number % divisor == 0:
                number //= divisor
            return number
        
        # factorize for permitted primes
        for factor in [2, 3, 5]:
            n = divide_until_fail(n, factor)
        
        return n == 1
    
    # Time: O(log(N)), Space: O(1)
    