class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper_func( a:List[int],n:int, speed:int) -> int:
            h=0
            for i in range(n):
                h+=a[i]//speed
                if a[i]%speed!=0:
                    h+=1
            return h
        n=len(piles)
        low,high=1,max(piles)
        res=-1
        while low<=high:
            guess=(low+high)//2
            hour=helper_func(piles,n,guess)
            if hour>h:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res