class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper_func(candies:List[int],guess:int,k:int,n:int)->bool:
            count=0
            for i in range(n):
                if candies[i]>=guess:
                    count+=candies[i]//guess
                    if count>=k:
                        return True
            return False
        low,high=1,max(candies)
        n=len(candies)
        res=0
        while low<=high:
            guess=(low+high)//2
            if helper_func(candies,guess,k,n):
                res=guess
                low=guess+1
            else:
                high=guess-1
        return res
