class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        highest = prices[0]

        for price in prices[1:]:
            if price >= highest:
                highest = price 
            else:
                profit += highest - lowest
                highest = price 
                lowest= price

        profit += highest - lowest
        return profit
