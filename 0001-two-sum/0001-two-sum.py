class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index in range(len(nums)): 
            if nums[index] in map:
                print(f"[{index},{ map.get(nums[index])}]") 
                return index, map.get(nums[index])
            diff = target - nums[index]
            if diff not in map:
                map[diff] = index



