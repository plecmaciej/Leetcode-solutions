class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        length = len(nums)
        score = 0
        for i in range(k):
            if i+k < length:
                if nums[i] > nums[i+k]:
                    score+= nums[i]
                    #print(nums[i])
            else:
                score += nums[i]
                #print(nums[i])
        
        for i in range(k, length):
            if nums[i] > nums[i-k]:
                if i+k < length:
                    if nums[i] > nums[i+k]:
                        score+= nums[i]
                        #print(nums[i])
                else:
                    score += nums[i]
                    #print(nums[i])

        return score 