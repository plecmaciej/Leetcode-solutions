class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        second_largest = 0

        while n > 0:
            actual = n % 10
            n = n // 10

            if actual > largest:
                second_largest = largest
                largest = actual
            elif actual > second_largest:
                second_largest = actual

            if largest == 9 and second_largest == 9:
                return 81
                
        return largest * second_largest
        