from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dict1 = Counter(s1)
        len1 = len(s1)
        
        for i in range(len(s2)):
            temp = s2[i:i+len1]
            
            dict2 = Counter(temp)
            
            if dict2 == dict1:
                return True
        return False
        