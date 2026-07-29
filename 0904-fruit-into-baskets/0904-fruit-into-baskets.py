class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        freq_map=dict()
        res=0
        low=0
        for high in range(len(fruits)):
            freq_map[fruits[high]]=freq_map.get(fruits[high],0)+1
            while len(freq_map)>2:
                freq_map[fruits[low]]-=1
                if freq_map[fruits[low]]==0:
                    del freq_map[fruits[low]]
                low+=1
            res=max(res,high-low+1)
        return res