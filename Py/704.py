class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)-1
        low = 0
        high = length
        
        while low<=high:
            mid = low + (high-low)//2
            
            if target == nums[mid]:
                return mid
            elif target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
                
        return -1