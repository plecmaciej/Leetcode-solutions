class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length1 = len(nums1)
        length2 = len(nums2)
        for i in range(length2):
            print(nums1[m+i], nums2[i])
            nums1[m+i] = nums2[i]
        nums1.sort()