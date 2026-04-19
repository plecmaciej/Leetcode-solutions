class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = [x for x in order if x in friends]
        return result