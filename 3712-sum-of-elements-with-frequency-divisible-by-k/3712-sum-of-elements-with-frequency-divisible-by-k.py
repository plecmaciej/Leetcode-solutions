class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        elements = {}
        output = 0
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
        
        for key, value in elements.items():
            if value % k == 0:
                output += value * key
        #print(elements)
        return output
