class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # Points to min
        r = 1  # Goes through every node to find maxProfit
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                l = r
            r += 1

        return maxProfit
