class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        count = 0
        i = 0
        while i < len(prices):
            sell_price = prices[i]
            buy_price = prices[count]
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit
            if count < i - 1:
                count += 1
            else:
                i += 1
                count = 0

        return max_profit