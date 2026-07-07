class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        sum=0
        res=0
        c=0
        while(n!=0):
            x=0
            while(x==0):
                x=n%10
                n=n/10
            sum+=x
            res=x*10**c+res
            c+=1
        return res*sum
