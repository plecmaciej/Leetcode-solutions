class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            copy = num 
            num = 0
            while copy > 0:
                num += copy % 10 
                copy = copy // 10
        return num