class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            summary = 0
            while num > 9:
                summary += num % 10
                num = num // 10
            summary += num
            if summary == i:
                return i

        return -1