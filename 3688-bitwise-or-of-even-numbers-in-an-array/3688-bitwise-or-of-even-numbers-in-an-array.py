class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            if num % 2 == 0:
                output = output | num 
        return output