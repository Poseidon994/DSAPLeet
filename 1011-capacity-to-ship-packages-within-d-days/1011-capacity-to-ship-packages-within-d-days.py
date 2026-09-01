class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper_func(weights:List[int],days:int, n:int, cap:int)->bool:
            ship=0
            for i in range(n):
                ship+=weights[i]
                if ship>=cap:
                    if ship>cap:
                        ship=weights[i]
                    else:
                        ship=0
                    days-=1
                    
            if ship!=0 and ship<=cap:
                days-=1
            if days<0:
                return False
            return True
        low,high=max(weights),sum(weights)
        res=-1
        while low<=high:
            guess=(low+high)//2
            if helper_func(weights,days,len(weights),guess):
                res=guess
                high=guess-1
            else:
                low=guess+1
        return res