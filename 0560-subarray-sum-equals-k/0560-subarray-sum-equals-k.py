class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f=dict()
        f[0]= 1
        Sum=0
        res=0
        for i in range(len(nums)):
            Sum+=nums[i]
            freq=f.get(Sum-k,0)
            res+=freq
            f[Sum]=f.get(Sum,0)+1

        return res