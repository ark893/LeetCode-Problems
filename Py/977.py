class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newarr = list()
        
        for i in nums:
            newarr.append(i**2)
        
        newarr.sort()
        
        return(newarr)