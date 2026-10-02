class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # slow = 0
        # fast = 0
        # profits = []
        # while fast < len(prices) - 1:
        #     if prices[slow + 1] < prices[slow]:
        #         slow += 1
        #         fast = slow
        #         profits.append(0)
        #     elif prices[fast + 1] > prices[fast]:
        #         fast += 1
        #     elif prices[fast + 1] < prices[fast] and prices[slow] > prices[fast + 1]:
        #         profits.append(prices[fast] - prices[slow])
        #         slow = fast + 1
        #         fast = slow
        #     else:
        #         fast += 1
        
        # profits.append(prices[fast] - prices[slow])
        # return max(profits)

        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit