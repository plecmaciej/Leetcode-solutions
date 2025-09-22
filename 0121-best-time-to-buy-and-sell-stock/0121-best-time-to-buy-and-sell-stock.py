class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = prices[0]
        low = prices[0]
        prev_diff = 0
        diff = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = prices [i]
            elif prices[i] > high:
                high = prices[i]
                if high - low > diff:
                    diff = high - low
        
        return diff