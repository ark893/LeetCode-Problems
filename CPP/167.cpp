class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int n = nums.size();
        vector<int> res(2);
        for( int i = 0; i<n; i++){
            
            int temp = target - nums[i];
            
            int l=i+1, r = n-1;
            
            while(l<=r){
                int mid = l+(r-l)/2;
                
                if(nums[mid] == temp){
                    res[0] = i+1;
                    res[1] = mid+1;
                    return res;
                }
                    
                
                else if(nums[mid]<temp)
                    l = mid+1;
                else
                    r=mid-1;
            }
        }
        return res;
    }
};