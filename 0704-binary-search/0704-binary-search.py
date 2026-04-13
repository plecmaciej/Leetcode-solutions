class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        if len(nums) == 0:
            return -1
        if nums[mid] == target:
            return mid
        else:
            if len(nums) == 1:
                return -1
            if nums[mid] > target:
                return self.search(nums[:mid], target)
            else:
                anwser = self.search(nums[mid + 1:], target)
                if anwser == -1:
                    return -1
                else:
                    return mid + 1 + anwser