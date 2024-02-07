class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Define left pointer for buying point
        left = 0

        # Define right pointer for selling point
        right = 0

        # Define max profit for calculation
        max_profit = 0

        # Define the length of the List(prices)
        length =  len(prices)

        # Loop until the right pointer reaches the end
        while right < length:
            # Check for profitability
            if prices[right] > prices[left]:
                # Calculate the max profit
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                # Set the previous low(left) to the new low(right)
                left = right
            # Increment the right pointer
            right += 1
        
        # Return the max profit
        return max_profit
