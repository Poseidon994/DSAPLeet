class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        have=dict()
        for i in s:
            have[i]=have.get(i,0)+1
        res = 0
        odd = False
        for char, val in have.items():
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                odd = True
        return res + 1 if odd else res