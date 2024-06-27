class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0  # Initialize the pointer for the next non-zero element position
        for i in range(len(nums)):  # Iterate through the array with pointer `i`
            if nums[i]:  # If the current element is non-zero
                nums[l], nums[i] = nums[i], nums[l]  # Swap the current element with the element at `l`
                l += 1  # Increment the pointer `l` to the next position
