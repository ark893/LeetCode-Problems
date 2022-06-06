class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        temp = [None] #O(1) extra space
        for i in range(k):
            temp[0] = nums.pop()
            nums.insert(0,temp[0])