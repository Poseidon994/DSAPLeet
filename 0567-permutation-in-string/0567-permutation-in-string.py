class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        have=dict()
        needed=dict()
        for i in s1:
            needed[i]=needed.get(i,0)+1
        required=len(needed)
        formed=0
        high=low=0
        while high<len(s1)+low and high<len(s2):
            have[s2[high]]=have.get(s2[high],0)+1
            if s2[high] in have and have[s2[high]]==needed.get(s2[high],0):
                formed+=1
            if formed==required:
                return True
            else:
                if high==(low+len(s1)-1):
                    
                    if s2[low] in have and have[s2[low]]==needed.get(s2[low],0):
                        formed-=1
                    have[s2[low]]-=1
                    low+=1
            high+=1
        return False