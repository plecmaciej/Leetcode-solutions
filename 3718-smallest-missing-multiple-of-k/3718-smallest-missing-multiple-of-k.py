class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiplies = [False] * ((100 // k) + 2)
        for i in range(len(nums)):
            if nums[i] % k == 0:
                 multiplies[nums[i]//k] = True

        #print(multiplies)

        for i in range(1,len(multiplies)):
            if multiplies[i] == False:
                return i * k     
        
