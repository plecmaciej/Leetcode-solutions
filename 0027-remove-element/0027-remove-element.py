class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        if right < 0:
            return 0
        while left < right:
            if nums[right] == val:
                right = right - 1
            elif nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
                right = right - 1
            else:
                left = left + 1
        if nums[left] != val:
            left = left + 1  
        return left 

