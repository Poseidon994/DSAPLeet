class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper_func(m:int,n:int,k:int,guess:int)->int:
            count=0
            row,col=n-1,0
            while row>=0 and col<m:
                if (row+1)*(col+1)<=guess:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count
        low,high=1,(m)*(n)
        res=-1
        while low<=high:
            guess=(low+high)//2
            ans=helper_func(m,n,k,guess)
            if ans>=k:
                res=guess
                high=guess-1
            else:
                low=guess+1
        return res