class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for i in range(32):
            ans = ans<<1
            if n&1:
                ans+=1
            n=n>>1
        return ans