class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=k=0
        while (i+k)<len(nums):
            if nums[i]==0:
                temp = nums.pop(i)
                nums.append(temp)
                k+=1
            else:
                i+=1

                