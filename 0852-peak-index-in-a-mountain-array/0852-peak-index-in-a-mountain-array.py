class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low,high=0,len(arr)-1
        res=-1
        while low<=high:
            guess=(low+high)//2
            if arr[guess]<arr[guess+1]:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res