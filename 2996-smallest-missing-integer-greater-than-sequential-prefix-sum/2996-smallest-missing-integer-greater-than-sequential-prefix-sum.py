class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                Sum+=nums[i]
                idx=i
            else:
                break
        if Sum not in nums:
            return Sum
        else:
            res=float('inf')
            for i in range(len(nums)):
                if Sum+i+1 not in nums:
                    return Sum+i+1
            return 