# Last updated: 10/21/2025, 2:03:24 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = prices[0]
        profit = 0
        for x in prices:
            if x > min:
                profit += x-min
            min = x


        return profit