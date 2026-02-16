class Solution:
    def mirrorDistance(self, n: int) -> int:
        copy = n 
        revers = 0 
        while copy is not 0:
            revers = revers * 10
            revers += copy % 10
            copy = copy // 10 
        return abs(n - revers)