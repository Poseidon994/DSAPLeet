class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f=dict()
        Sum=0
        res=0
        f[0]=1
        for i in range(len(nums)):
            Sum+=nums[i]
            rem=Sum%k
            if rem<0:
                rem+=k
            res+=f.get(rem,0)
            f[rem]=f.get(rem,0)+1
        return res