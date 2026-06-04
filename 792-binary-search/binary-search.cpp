class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = std::size(nums)-1;

        while(low<=high){
            int mid = (high+low)/2;
            int guess = nums[mid];

            if (guess == target){
                return mid;
            }
            else if (guess > target){
                high = mid-1;
            }
            else if ( guess < target){
                low = mid+1;
            }
            
        }
        return -1;
    }
};