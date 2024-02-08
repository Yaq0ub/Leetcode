class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman dictionary
        R = {"I": 1, "V": 5, "X": 10, "L": 50, 
             "C": 100, "D": 500, "M": 1000}
        
        # Define sum variable
        sum = 0

        # Loop through the input string
        for i in range(len(s) - 1):
            # Check if to subtract or add
            if R[s[i]] < R[s[i+1]]:
                sum -= R[s[i]]
            else:
                sum += R[s[i]]
                
        # return the sum + the last roman value
        return sum + R[s[len(s)-1]]