class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        int n = nums.size();
        vector<int> copy(n);
            
        if ( (n==0) || (k<=0) )
            return;
        
        for(int i=0; i<n; i++)
            copy[i] = nums[i];
        
        //rotating
        
        for(int i=0; i<n; i++){
            nums[(i+k)%n] = copy[i];
        }
    }
};