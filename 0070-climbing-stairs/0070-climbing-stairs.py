class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 2
        z = 3
        if n <=3:
            return n 
        while n > 3:
            x = y
            y = z 
            z = x + y
            n -= 1
        return z
