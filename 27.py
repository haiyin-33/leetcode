class Solution:
    def removeElement(self, nums,val):
        length=len(nums)-1
        if(length>=0):
            for i in range(length):
                if(nums[length-i]==val):
                    del nums[length-i]
            if(nums[0]==val):
                del nums[0]
        else:
            return 0
        return len(nums)