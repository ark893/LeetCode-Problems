class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a=b=1
        for _ in range(n):
            a,b = b, b+a
        return a