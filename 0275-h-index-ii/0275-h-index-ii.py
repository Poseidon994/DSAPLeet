class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def helper_func(citations:List[int],h:int,n:int)->bool:
            count=0
            for i in range(n):
                if citations[i]>=h:
                    count+=1
                if count==h:
                    return True
            return False
        low,high=1,min(max(citations),len(citations))
        res=0
        n=len(citations)
        while low<=high:
            guess=(low+high)//2
            if helper_func(citations,guess,n):  
                res=guess
                low=guess+1
            else:
                high=guess-1
        return res