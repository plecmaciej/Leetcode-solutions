class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1:
            nums[0] = nums[0] % 2
            return nums

        left = 0 
        right = length -1

        while left < right:
            modulo_left = nums[left] % 2

            if modulo_left == (nums[right] % 2):
                if modulo_left == 0:
                    nums[left] = 0
                    left += 1

                    while (nums[left] % 2) != 1 and (left < right):
                        nums[left] = 0
                        left += 1

                else:
                    nums[right] = 1
                    right -= 1

                    while (nums[right] % 2) != 0 and (left < right):
                        nums[right] = 1
                        right -= 1

            if left < right:
                nums[left] = 0
                nums[right] = 1
                left += 1
                right -= 1

        nums[left] = (nums[left] % 2)

        return nums
