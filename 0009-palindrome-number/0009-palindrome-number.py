class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        elif x == 0:
            return True 
        elif x < 1:
            return False
        else:
            half = 0
            number_of_digits = math.floor(math.log10(abs(x))) + 1
            if number_of_digits == 1:
                return True
            for i in range(number_of_digits//2):
                rest = x % 10 
                half = half * 10
                half += rest
                x = x // 10
            if number_of_digits % 2 == 1:
                 x = x // 10
            if half == x:
                return True
            else:
                return False
            #map = {}
            #for i in range(number_of_digits):
            #    map[i] = x % 10
            #    x = x // 10 
            #for i in range(number_of_digits//2):
            #    if map[i] != map[number_of_digits - i - 1]:
            #        return False
            return True 
        