class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        low=0
        res=float('inf')
        l=0
        start=0
        have=dict()
        needed=dict()
        for i in t:
            needed[i]=needed.get(i,0)+1
        required=len(needed)
        formed=0
        for high in range(len(s)):
            have[s[high]]=have.get(s[high],0)+1
            if s[high] in needed and have[s[high]]==needed[s[high]]:
                formed+=1
            while formed==required:
                l=high-low+1
                if s[low] in needed and have[s[low]]==needed[s[low]]:
                    formed-=1
                if res>l:
                    res=l
                    start=low
                have[s[low]]-=1
                low+=1
        return s[start:start+res] if res!=float('inf') else ""