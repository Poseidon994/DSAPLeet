class Solution(object):
    def square(self,n):
        sum=0
        while(n!=0):
            sum=sum+(n%10)**2
            n=n//10
        return sum
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow=n
        fast=n
        while (fast!=1):
            slow=self.square(slow)
            fast=self.square(fast)
            fast=self.square(fast)
            if slow==fast and slow!=1:
                return False
        return True

        