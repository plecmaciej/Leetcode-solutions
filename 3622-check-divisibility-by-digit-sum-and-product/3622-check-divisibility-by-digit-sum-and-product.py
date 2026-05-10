class Solution:
    def checkDivisibility(self, n: int) -> bool:
        value = n
        product = summary = n % 10
        n = n // 10
        while n > 0:
            modulo = n % 10
            summary += modulo
            product *= modulo
            n = n // 10


        return value % (summary + product) == 0

