class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = ''
        maximum = 0
        for i in s:
            if i not in letters:
                letters+=i
                
                if len(letters)>maximum:
                    maximum = len(letters)
                    
            else:
                letters = letters[letters.find(i)+1:]+i
            
        return maximum