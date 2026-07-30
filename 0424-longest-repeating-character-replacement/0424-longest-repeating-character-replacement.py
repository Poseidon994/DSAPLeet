class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low=0
        res=0
        freq_map=dict()
        max_freq=0
        for high in range(len(s)):
            freq_map[s[high]]=freq_map.get(s[high],0)+1
            max_freq=max(max_freq,freq_map[s[high]])
            while (high-low+1)-max_freq>k:
                freq_map[s[low]]-=1
                if freq_map[s[low]]==0:
                    del freq_map[s[low]]
                low+=1
            res=max(res,high-low+1)
        return res