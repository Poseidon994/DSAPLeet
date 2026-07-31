class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bestending=nums[0]
        ans1=nums[0]
        ans2=nums[0]
        sum=nums[0]
        for i in range(1,len(nums)):
            sum+=nums[i]
            v1=nums[i]
            v2=bestending+nums[i]
            bestending=min(v1,v2)
            ans1=min(ans1,bestending)
        bestending=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=bestending+nums[i]
            bestending=max(v1,v2)
            ans2=max(ans2,bestending)
        
        if sum==ans1:
            return ans2
        return max(ans2,sum-ans1)