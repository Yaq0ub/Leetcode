'''
Steps:
1 - Pick the min string lengths of each str1&str2 for iteration
2 - Iterate from the end of the string till the beginning
3 - On each iteration, pick the current length(l) of the substring
and check if its a divisor of both str1 and str2. If it is go to step 4
4 - Check if the substring at length l can form each of the strings by 
multiplying the sub string with the quotients resulting from str1/l &
str2/l
5 - If both strings can be formed by substring at length l then
we have found the gcd
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        
        def isDivisor(l):
            if l1%l != 0 or l1%l != 0:
                return False
            substr = str1[:l]
            factor1, factor2 = l1//l, l2//l
            if str1 == (factor1*substr) and str2 == (factor2*substr):
                return True
            else: 
                return False

        for l in range(min(l1,l2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""

        