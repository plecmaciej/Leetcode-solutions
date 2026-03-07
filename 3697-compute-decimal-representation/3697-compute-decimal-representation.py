class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        power = 1
        output = []
        while n > 0:
            base = (n%10)
            if base != 0:
                output.append(base * power)
            power *= 10
            n = n // 10
        return output[::-1]