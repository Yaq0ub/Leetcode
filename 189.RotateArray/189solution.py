class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Method to reverse an array
        def reverse_array(arr: List[int], st: int, ed: int) -> List[int]:
            while st < ed:
                arr[st],arr[ed] = arr[ed], arr[st]
                st += 1
                ed -= 1
            return arr

        # Length of the List
        l = len(nums)

        # If K is greater than the length
        k = k % l

        # Reverse all the array
        nums = reverse_array(nums, 0, l - 1)

        # Reverse  first K elements
        nums = reverse_array(nums, 0, k-1)

        # Reverse the remaining array
        nums = reverse_array(nums, k, l - 1)
        