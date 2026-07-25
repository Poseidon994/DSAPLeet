class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        min_diff=float('inf')
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low,high=i+1,len(nums)-1
            sum=0
            
            while(low<high):
                sum=nums[i]+nums[low]+nums[high]
                if sum==target:
                     return sum
                else:
                    diff=abs(sum-target)
                    if diff<min_diff:
                        ans=sum
                        min_diff=diff
                    if sum<target:
                        low+=1
                    else:
                        high-=1     
        return ans    