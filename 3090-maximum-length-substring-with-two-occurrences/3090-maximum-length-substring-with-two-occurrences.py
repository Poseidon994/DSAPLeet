class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        f=dict()
        low=0
        res=0
        for high in range(len(s)):
            f[s[high]]=f.get(s[high],0)+1
            if f[s[high]]>2:
                while(f[s[high]]>2):
                    f[s[low]]-=1
                    if f[s[low]]==0:
                        del f[s[low]]
                    low+=1
            res=max(res,high-low+1)
        return res