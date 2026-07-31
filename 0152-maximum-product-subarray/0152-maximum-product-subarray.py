class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_ending=nums[0]
        min_ending=nums[0]
        ans=nums[0]
        for i in range(1, len(nums)):
            v1=best_ending*nums[i]
            v2=min_ending*nums[i]
            v3=nums[i]
            best_ending=max(v1,max(v2,v3))
            min_ending=min(v1,min(v2,v3))
            ans=max(best_ending,min_ending,ans)
        return ans