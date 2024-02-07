class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Define profit for calculation
        profit = 0

        # Get the length of prices
        length = len(prices)

        # Loop through prices list starting from index 1,
        # Because we will be comparing it to the previous index
        for i in range(1, length):
            # Check for profitability
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]
        
        # Return the profit
        return profit