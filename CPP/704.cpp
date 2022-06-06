class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int high, low=0, mid;
        
        high = nums.size()-1;
        
        while(low<=high){
            mid = (high-low)/2 + low;
            
            if(target == nums[mid])
                return mid;
            
            else if(target>nums[mid])
                low = mid+1;
            
            else
                high = mid-1;
            
        }
        
        return (-1);
        
    }
};