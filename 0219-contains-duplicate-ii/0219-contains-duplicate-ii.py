class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_of_numbers = {}
        for i in range(len(nums)):
            if nums[i] not in map_of_numbers:
                map_of_numbers[nums[i]] = i
            else:
                if abs(map_of_numbers[nums[i]] - i) <= k:
                    return True
                else:
                    map_of_numbers[nums[i]] = i

        return False