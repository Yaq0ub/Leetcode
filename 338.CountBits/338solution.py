class Solution:
    def countBits(self, n: int) -> List[int]:
        # Step 1: Initialize the result array with zeros
        ans = [0] * (n + 1)
        
        # Step 2: Loop through each number from 1 to n
        for i in range(1, n + 1):
            # ans[i >> 1] gives the number of 1's in the binary representation of i // 2
            # i & 1 checks if the least significant bit is 1 (i.e., if i is odd)
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans

# Example usage
solution = Solution()
n = 5
print(solution.countBits(n))  # Output: [0, 1, 1, 2, 1, 2]