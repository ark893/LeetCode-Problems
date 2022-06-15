class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        
        if len(nums) == 0:
            return 0
        
        prev1=prev2=0
        
        for num in nums:
            temp = prev1
            prev1 = max(prev2+num, prev1)
            prev2 = temp
            
        return prev1