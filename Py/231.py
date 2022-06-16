class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n and not(n & n-1):
            return True
        return False