class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prevNumber = -101
        i = 0
        j = 0 
        length = len(nums)
        while i < length:
            if nums[i] != prevNumber:
                #nums.pop(j)
                prevNumber = nums[i]
                if j != i:
                    nums[i],nums[j] = nums[j], nums[i]
                j = j + 1
            i = i + 1
        #j = j + 1
        return j

        