class Solution:
    def sumAndMultiply(self, n: int) -> int:
        counter = 0
        sume = 0
        x = 0
        while n > 0:
            if n % 10 is not 0:
                x = pow(10, counter) * (n % 10) + x
                sume += n % 10 
                counter += 1
            n = n // 10
        
        return x * sume