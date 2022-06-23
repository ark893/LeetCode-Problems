class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        x=0
        for i in t:
            if x<len(s):
                if i == s[x]:
                    x+=1
                
        if x==len(s):
            return True
        return False