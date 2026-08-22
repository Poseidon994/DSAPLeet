class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n1=n
        p,s=1,0
        while n1:
            d=n1%10
            s+=d
            p*=d
            n1//=10
        return True if n%(s+p)==0 else False