class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        have=dict()
        needed=dict()
        for i in p:
            needed[i]=needed.get(i,0)+1
        required=len(needed)
        formed=0
        high=low=0
        res=[]
        while high<len(p)+low and high<len(s):
            have[s[high]]=have.get(s[high],0)+1
            if s[high] in have and have[s[high]]==needed.get(s[high],0):
                formed+=1
            if formed==required:
                res.append(low)
            
            if high==(low+len(p)-1):
                if s[low] in have and have[s[low]]==needed.get(s[low],0):
                        formed-=1
                have[s[low]]-=1
                low+=1         
            high+=1
        return res
        