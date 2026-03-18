class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = ""
        if num == 0:
            return "0"
        if num > 0:
            while num >0:
                base7 =  str(num % 7) + base7
                num = num // 7
        else:
            num = -num
            while num > 0:
                base7 =  str(num % 7) + base7
                num = num // 7
            base7 =  "-" + base7

        return base7