class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_max=-1
        right_max=float('-inf')
        for i in range(len(nums)):
            if nums[i]<right_max:
                index_max=i
            else:
                right_max=nums[i]
        left_min=float('inf')
        index_min=-1
        for j in range(len(nums)-1,-1,-1):
            if nums[j]>left_min:
                index_min=j
            else:
                left_min=nums[j]
        if index_max == -1:
            return 0
        return index_max-index_min+1