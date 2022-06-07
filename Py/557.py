class Solution:
    def reverseWords(self, s: str) -> str:
        news = ""
        wordlist = s.split()
        for i in range(len(wordlist)):
            x = wordlist[i]
            temp = x[::-1]
            if i==(len(wordlist)-1):
                news+=temp
            else:
                news+=temp+' '
            
        return news