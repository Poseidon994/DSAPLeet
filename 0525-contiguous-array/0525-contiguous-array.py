class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=dict()
        res=0
        zero=0
        one=0
        f[0]=-1
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            # if diff==0:
            #     res=max(res, i+1)
            #     continue
            if diff not in f:
                f[diff]=i
            else:
                idx=f[diff]
                l=i-idx
                res=max(res,l)
        return res