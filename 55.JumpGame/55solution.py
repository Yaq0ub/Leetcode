class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Set the last element as reachable
        reachable = len(nums) - 1

        # Apply a greedy algorithm
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= reachable:
                reachable = i
                
        return True if reachable == 0 else False