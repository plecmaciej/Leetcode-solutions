class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a = -101
        b = -101
        c = nums[0]
        for num in nums:
            
            if num > b:
                if num > a:
                    if b != -101:
                        if b < c:
                            c = b
                    a, b = num, a
                else:
                    if b != -101:
                        if b < c:
                            b,c = num,b
                        else:
                            b = num
                    else:
                        b = num
            elif num < c:
                c = num
        return a+b-c