class Solution:
    def maxProduct(self, n: int) -> int:
        highest_1 = 0
        highest_2 = 0
        actual = 0
        while n > 0:
            actual = n % 10
            n = n // 10
            if actual > highest_1:
                highest_2 = highest_1
                highest_1 = actual
            elif actual > highest_2:
                highest_2 = actual
            
        return highest_1 * highest_2
        