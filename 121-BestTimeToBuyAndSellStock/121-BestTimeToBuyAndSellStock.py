# Last updated: 10/21/2025, 2:03:25 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = prices[0]
        profit = 0
        for x in prices:
            if x < min:
                min = x
                max = 0
            if x > max:
                max = x
            if max-min > profit:
                profit = max-min

        return profit