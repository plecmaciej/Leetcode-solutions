# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(1) == True:
            return 1
        else:
            start = 1
        end = n
        while end - start > 1:
            middle = (start + end) // 2
            if isBadVersion(middle):
                end = middle
            else:
                start = middle
        return end