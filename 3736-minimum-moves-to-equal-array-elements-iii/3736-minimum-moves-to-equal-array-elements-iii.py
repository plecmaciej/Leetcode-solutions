class Solution:
    def minMoves(self, nums: List[int]) -> int:
        highest = nums[0]
        minimum_total = 0
        for i in range(0, len(nums)):
            if nums[i] < highest:
                minimum_total += highest - nums[i]
            elif nums[i] > highest:
                minimum_total += i * (nums[i] - highest)
                highest = nums[i]
            #print(minimum_total, nums[i], highest)
            
        return minimum_total