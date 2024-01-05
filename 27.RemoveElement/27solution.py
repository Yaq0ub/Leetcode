'''
1 - A counter that starts from the first index and is 
incremented whenever the current value does not equal to val
2 - The current index will always be increment scanning for
an int that does not equal to val
3 - If step 2 is satisfied then we swap nums[counter](the current
item that equals to val)
4 - return k because it represents the last element that is not
equal to val
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter+=1
        return counter