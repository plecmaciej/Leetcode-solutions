class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = True
        output = 0
        for num in nums:
            if even:
                output += num
                even = False
            else:
                output -= num
                even = True
        return output
