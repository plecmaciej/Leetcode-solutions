class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        if nums[right]<target:
            return right + 1
        if nums[left] > target:
            return left
        position = right//2
        if nums[position] == target:
            return position
            
        while left+1 < right:
            if nums[position] > target:
                right = position 
            else:
                left = position 

            position = (right + left)//2

            if nums[position] == target:
                return position
        return left + 1