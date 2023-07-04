class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if len(prices) == 1:
        #     return 0

        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):

        #         if prices[i] > prices[j]:
        #             continue
        #         elif prices[i] < prices[j]:
        #             profit = max(profit, prices[j] - prices[i])

        # return profit

        if len(prices) == 1:
            return 0

        min_price = prices[0]  # Minimum price encountered so far
        max_profit = 0  # Maximum profit

        for price in prices:
            if price < min_price:
                # If current price is lower than the minimum price, update the minimum price
                min_price = price
            else:
                # Calculate the profit if we sell at the current price
                current_profit = price - min_price
                # Update the maximum profit if the current profit is higher
                max_profit = max(max_profit, current_profit)

        return max_profit