/**
Steps:
1 - two pointers will be required to be able to check if the
previous element does not equal to the current one
2 - K wil be pointing at the previous element place holder that
can be swapped.
3 - Once we encounter a non equal element where nums[i]!=nums[i-1],
we know nums[k] can be swapped with nums[i]
*/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k=1, l = nums.size();
        for(int i = 1; i < l; i++){
            if(nums.at(i) != nums.at(i-1)){
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};