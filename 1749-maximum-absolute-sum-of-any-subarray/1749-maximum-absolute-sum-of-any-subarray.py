class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        min_sum=nums[0]
        res=abs(nums[0])
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=nums[i]+max_sum
            v3=nums[i]+min_sum
            max_sum=max(v1,max(v2,v3))
            min_sum=min(v1,min(v2,v3))
            res=max(abs(res),abs(max_sum),abs(min_sum))
        return res