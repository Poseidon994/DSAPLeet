class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        m1,m2=max(nums),min(nums)
        id1,id2=0,0
        for i in range(len(nums)):
            if nums[i]==m1:
                id1=i
            if nums[i]==m2:
                id2=i
        if id1==id2:
            return 1
        
        res=min(max(id1,id2)+1,len(nums)-min(id1,id2),min(id1,id2) + 1 + (len(nums) - max(id1,id2)) )
        return res