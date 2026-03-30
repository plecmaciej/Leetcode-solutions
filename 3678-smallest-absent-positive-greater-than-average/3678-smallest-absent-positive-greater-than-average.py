class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        summary =  sum(nums)
        n = len(nums)
        avg = summary / n
        if avg < 0:
            avg_ceil = 1
        else:
            avg_ceil = int(avg) + 1
        
        while True:
            if avg_ceil in nums:
                avg_ceil += 1
            else:
                return avg_ceil 