class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        common = []
        for element in (counter1 & counter2).elements():
            common.append(element)

        return common