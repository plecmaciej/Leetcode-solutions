class Solution:
    def isHappy(self, n: int) -> bool:
        values_map = {}
        new_num = 0
        while n != 1:
            while n > 0:
                new_num += pow((n % 10), 2)
                n = n // 10
            if new_num not in values_map:
                values_map[new_num] = True
            else:
                return False
            n = new_num
            new_num = 0
        return True