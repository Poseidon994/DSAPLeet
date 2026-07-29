class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum=[0]*(len(nums))
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return (min(nums)*(-1))+1 if min(nums)<1 else 1
        