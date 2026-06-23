from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        c = Counter(s)
        amount = len(c)
        if amount <= k:
            return 0
        else:
            least_common = c.most_common()[::-1][:(amount -k)]

            return sum(num for _, num in least_common)


