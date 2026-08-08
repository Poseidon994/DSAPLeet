class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        have=dict()
        for i in s:
            have[i]=have.get(i,0)+1
        odd= False
        res=0
        for char,val in have.items():
            if val%2==0:
                res+=val
            else:
                odd=True
        if not odd:
            return res
        for char, val in have.items():
            if val%2==1:
                res+=val-1
        return res+1
        