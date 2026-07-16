class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minimal = cost[0]
        for i in range(1, len(cost)):
            if cost[i] < minimal:
                minimal = cost[i]
            else:
                cost[i] = minimal
        
        return cost