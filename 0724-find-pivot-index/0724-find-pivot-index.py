class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        Sum=sum(nums)
        for i in range(len(nums)):
            right=Sum-nums[i]-left
            if right==left:
                return i
            left+=nums[i]
        return -1