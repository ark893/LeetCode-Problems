class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s)-1
        
        while i>=0:
            #print(s.pop(len(s)-i-1))
            s.insert(0,s.pop(len(s)-i-1))
            i-=1