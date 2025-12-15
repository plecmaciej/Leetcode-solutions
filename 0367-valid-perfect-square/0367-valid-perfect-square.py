class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 2 or num == 4 :
            return True
        for i in range(3, num//2):
            power = i * i
            if power == num:
                return True
            elif power > num:
                return False

        return False