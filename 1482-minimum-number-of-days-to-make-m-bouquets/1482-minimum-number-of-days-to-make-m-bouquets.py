class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper_func(bloomDay:List[int],day:int,k:int,m:int,n:int)->bool:
            count=0
            for i in range(n):
                if bloomDay[i]<=day:
                    count+=1
                    if count==k:
                        m-=1
                        count=0
                        if m==0:
                            return True
                    continue
                count=0
            return False           
        low,high=min(bloomDay),max(bloomDay)
        n=len(bloomDay)
        res=-1
        while low<=high:
            guess=(low+high)//2
            if helper_func(bloomDay,guess,k,m,n):
                res=guess
                high=guess-1
            else:
                low=guess+1
        return res