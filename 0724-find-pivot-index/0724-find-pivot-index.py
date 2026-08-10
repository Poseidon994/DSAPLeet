class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        Sum=sum(nums)
        for i in range(len(nums)):
            if i>0:
                left+=nums[i-1]
            right=Sum-nums[i]-left
            if right==left:
                return i
        return -1