# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
#
# Example 1:
#
# Input: prices = [10,1,5,6,7,1]
#
# Output: 6
#
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
#
# Example 2:
#
# Input: prices = [10,8,7,5,2]
#
# Output: 0
#
# Explanation: No profitable transactions can be made, thus the max profit is 0.
#
# Constraints:
#
#     1 <= prices.length <= 100
#     0 <= prices[i] <= 100
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        min_seen = prices[0]
        max_seen = prices[1]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_seen:
                min_seen = prices[i]
            if prices[i] > max_seen:
                max_seen = prices[i]
            if prices[i] - min_seen > max_profit:
                max_profit = prices[i] - min_seen

        return max_profit

