class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        no_double = list(dict.fromkeys(nums))
        no_double.sort()
        if len(no_double) >= 3:
            return no_double[-3]
        else:
            return no_double[-1]