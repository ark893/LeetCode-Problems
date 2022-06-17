class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        
        for i in nums:
            ans^=i
        
        return ans

#this works because XOR of two same numbers is 0. Thus, when we XOR all numbers in list, we will find the number that is present only once
