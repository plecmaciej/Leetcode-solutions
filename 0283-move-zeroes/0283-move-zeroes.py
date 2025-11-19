class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        while left < len(nums) - 1 and nums[left] != 0 :
            left +=1
        right = left + 1 
        while right < len(nums):
            while nums[left] != 0:
                left +=1
            while nums[right] == 0:
                right +=1
                if right >= len(nums):
                    return 
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right +=1

        