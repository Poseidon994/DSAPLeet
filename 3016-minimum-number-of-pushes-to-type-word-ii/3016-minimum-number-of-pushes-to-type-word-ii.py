class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq_map=dict()
        for ch in word:
            freq_map[ch]=freq_map.get(ch,0)+1
        freqs = sorted(freq_map.values(), reverse=True)

        total = 0
        for idx, f in enumerate(freqs):
            push_cost = idx // 8 + 1
            total += f * push_cost
        return total