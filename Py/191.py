class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # c=0
        # while n:
        #     n&=n-1
        #     c+=1
        # return c

        # Above solutiom is the same, but the way it works is by using bit manipulation, quite literally
        # assume n=4, bin(n)=0b100. bin(n-1)=0b011. bin(n&n-1)=0b000. Therefore, c=1. Because & operation removes last significant '1'.
        # we count number of significant '1's
        
        x=bin(n)
        
        return x.count('1')