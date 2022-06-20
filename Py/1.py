class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            x = target-nums[i]
            
            if x in nums:
                for j in range(i+1, len(nums)):
                    if x==nums[j]:
                        return [i,j]

            #this solution is faster, but it is not the best solution. Best is dictionary.
                    
            # for j in range(i+1, len(nums)):
            #     if x==nums[j]:
            #         return [i,j]


