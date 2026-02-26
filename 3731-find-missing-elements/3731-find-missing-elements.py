class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum = nums[0]
        maximum = nums[0]
        arr = [False] * 101

        for num in nums:
            if num > maximum:
                maximum = num
            elif num < minimum:
                minimum = num
            arr[num] = True
        
        missing = []
        for i in range(minimum, maximum):
            if arr[i] == False:
                missing.append(i)

        return missing