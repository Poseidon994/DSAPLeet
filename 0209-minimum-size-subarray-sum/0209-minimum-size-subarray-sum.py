class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        low=0
        res=float('inf')
        for high in range(len(nums)):
            sum+=nums[high]
            while sum>=target:
                res=min(high-low+1,res)
                sum-=nums[low]
                low+=1
        return res if res != float('inf') else 0