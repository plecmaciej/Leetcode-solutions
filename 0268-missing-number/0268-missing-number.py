class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1 
        if nums[end] == end:
            return end+1
        middle = 0
        while start < end :
            middle = (start + end) // 2
            if nums[middle] == middle:
                start = middle + 1 
            else:
                end = middle
        return nums[start] - 1