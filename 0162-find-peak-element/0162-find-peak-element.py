class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        res=-1
        while low<=high:
            guess=(low+high)//2
            if guess==len(nums)-1:
                res=guess
                break
            if nums[guess]<nums[guess+1]:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res