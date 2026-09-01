class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper_func(nums: List[int], k: int, cap:int, n:int)->bool:
            count=0
            for i in range(n):
                count+=nums[i]
                if count>=cap:
                    if count>cap:
                        count=nums[i]
                    else:
                        count=0
                    k-=1
            if count!=0 and count<=cap:
                k-=1
            if k<0:
                return False
            return True
        low,high=max(nums),sum(nums)
        res=0
        while low<=high:
            guess=(low+high)//2
            if helper_func(nums,k,guess,len(nums)):
                res=guess
                high=guess-1
            else:
                low=guess+1
        return res