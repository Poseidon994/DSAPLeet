class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros=0
        low=0
        res=0
        for high in range(len(nums)):
            if nums[high]==0:
                zeros+=1
            while zeros>k:
                if nums[low]==0:
                    zeros-=1
                low+=1
            res=max(res,high-low+1)
        return res