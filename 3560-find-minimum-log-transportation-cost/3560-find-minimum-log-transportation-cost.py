class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cost = 0
        if n > k:
            cost += (n-k) * k
        elif m > k:
            cost += (m-k) * k
        return cost
        