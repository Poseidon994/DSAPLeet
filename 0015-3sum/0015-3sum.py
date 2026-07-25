class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        a=set()
        for i in range(len(nums)):
            k=nums[i]
            low,high=i+1,len(nums)-1
            while(low<high):
                if nums[low]+nums[high]+k==0:
                    a.add((k,nums[low],nums[high]))
                    low+=1
                    high-=1
                    continue
                elif nums[low]+nums[high]+k<0:
                    low+=1
                else:
                    high-=1
        return [list(t) for t in a]
                


