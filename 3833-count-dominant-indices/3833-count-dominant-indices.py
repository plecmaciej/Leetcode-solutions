class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        avg = sum(nums)
        items = len(nums)
        dominant = 0 
        for i in range(0, items-1):
            avg = avg - nums[i]
            items -= 1
            if avg/items < nums[i]:
                dominant += 1
        return dominant