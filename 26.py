class Solution:
    def removeDuplicates(self,nums):
        num2=nums.copy()
        for i in num2:
            if(int(nums.count(i))==1):
                continue
            else:
                nums.remove(i)
        return len(nums)