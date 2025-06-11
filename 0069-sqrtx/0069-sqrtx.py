class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        left = 0
        right = x
        number = 0
        power = 0
        while right > left + 1:
            number = (right + left)//2
            power = number * number
            if power > x:
                right = number
            else:
                left = number

        if power > x :
            number = number - 1

        return number  
