class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        first = 0 
        second = 1 
        maxprofit = 0

        while second < len(prices):
            if prices[first] < prices[second]:
                diff = prices[second] - prices[first]
                maxprofit = max(maxprofit , diff)
            else :
                first = second
            second = second + 1 
        return maxprofit

  