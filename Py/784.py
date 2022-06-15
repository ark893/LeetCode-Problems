class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        
        def back(sub="", i=0):
            
            if len(sub)==len(s):
                res.append(sub)
                
            else:
                if s[i].isalpha():
                    back(sub+s[i].swapcase(), i+1)
                    
                back(sub+s[i], i+1)
                
        res=[]
        back()
        return res