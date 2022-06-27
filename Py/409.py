from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)
    
#         values = Counter(s).values()
#         length = 0
        
#         for val in values:
#             if val%2==1:
#                 length+=val
            
#         return len(s)-length+bool(length)

# Don't understand why my solution didn't work. Is literally the same