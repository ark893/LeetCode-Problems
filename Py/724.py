class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        newarr=list()
        tot=0
        for i in range(len(nums)):
            newarr.append(tot)
            tot+=nums[i]
        
        for i in range(len(nums)):
            left = newarr[i]
            right = tot-nums[i]-left
            
            if left == right:
                return i
            
        return -1