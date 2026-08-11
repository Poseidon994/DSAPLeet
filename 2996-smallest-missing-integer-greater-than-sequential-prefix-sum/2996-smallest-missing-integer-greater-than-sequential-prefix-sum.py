class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                Sum+=nums[i]
                idx=i
            else:
                break
      
        num_set = set(nums)
        candidate = Sum
        while candidate in num_set:
            candidate += 1
        return candidate