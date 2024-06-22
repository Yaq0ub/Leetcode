class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Normalize spaces by trimming and splitting, then rejoining with a single space
        # Convert the string to a list of characters to allow in-place modification
        s = list(' '.join(s.strip().split()))

        # Step 2: Helper function to reverse the characters in the list from index `start` to `end`
        def reverse(strg, start, end):
            while start < end:
                strg[start], strg[end] = strg[end], strg[start]
                start += 1
                end -= 1

        # Step 3: Reverse the entire list of characters
        reverse(s, 0, len(s) - 1)

        # Step 4: Reverse each word in the reversed list
        l = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(s, l, i - 1)  # Reverse the current word
                l = i + 1  # Move to the start of the next word
        # Reverse the last word
        reverse(s, l, len(s) - 1)

        # Step 5: Convert the list of characters back to a string
        return ''.join(s)

# Example usage
solution = Solution()
s = "  hello   world  "
print(f"'{solution.reverseWords(s)}'")  # Output: 'world hello'
