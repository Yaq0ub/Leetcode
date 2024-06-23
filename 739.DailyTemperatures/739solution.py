class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with zeros
        result = [0] * len(temperatures)
        
        # Initialize the stack to keep track of temperatures and their indices
        stack = []
        
        # Iterate through the temperatures with their indices
        for i, t in enumerate(temperatures):
            # While stack is not empty and the current temperature is higher than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                # Pop the top of the stack
                stackT, stackI = stack.pop()
                # Calculate the number of days until a warmer temperature
                result[stackI] = i - stackI
            # Push the current temperature and its index onto the stack
            stack.append((t, i))
        
        return result
