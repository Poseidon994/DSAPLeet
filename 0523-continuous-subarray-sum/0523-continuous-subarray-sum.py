class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        f=dict()
        f[0]=-1
        Sum=0
        res=0
        for i in range(len(nums)):
            Sum+=nums[i]
            rem=Sum%k
            if rem<0:
                rem=rem+k
            res+=f.get(rem,0)
            if rem in f and i-f[rem]>=2:
                return True
            if rem not in f:
                f[rem]=f.get(rem,i)
        return False