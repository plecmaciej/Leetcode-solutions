from collections import Counter

class Solution:
    def isPrime(self, value: int) -> bool:
        if (value < 2):
            return False
        elif (value == 2):
            return True
        elif (value % 2 == 0): 
            return False
        else:
            sqrtt =  int(sqrt(value))

            for i in range(3, sqrtt + 1, 2):

                if (value % i == 0):
                    return False
                
            return True


    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        elements = Counter(nums)
        for frequency in elements.values():  

            if self.isPrime(frequency):
                return True

        return False