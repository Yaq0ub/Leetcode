class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Define hash map for the occurrences count
        occ = {}
        
        # Loop over the nums array and count the occurrences
        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        
        # Get the key that has the max value
        max_key = max(occ, key=occ.get)

        #return the key with the max value
        return max_key