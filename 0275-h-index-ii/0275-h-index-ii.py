class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low,high=0,len(citations)-1
        res=0
        n=len(citations)
        if n==1:
            if citations[0]:
                return 1
            else:
                return 0
        while low<=high:
            guess=(low+high)//2
            if n-guess<=citations[guess]: 
                res=n-guess
                high=guess-1
            else:
                low=guess+1
        return res