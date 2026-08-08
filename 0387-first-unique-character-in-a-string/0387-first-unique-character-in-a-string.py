class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        f=dict()
        for i in s:
            f[i]=f.get(i,0)+1
        for i in range(len(s)):
            if f[s[i]]==1:
                return i
        return -1