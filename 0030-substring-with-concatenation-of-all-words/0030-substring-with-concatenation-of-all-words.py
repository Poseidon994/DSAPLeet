class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len=len(words[0])
        num_words=len(words)
        window_len=word_len*num_words
        word_count=Counter(words)
        if len(word_count) == 1:
            target = words[0]
            c = []

            for i in range(len(s) - window_len + 1):
                if s[i:i + window_len] == target * num_words:
                    c.append(i)

            return c
        window=[""]*num_words
        low=0
        res=[]
        high=window_len
        while high<=len(s):
            idx=low
            for i in range(num_words):
                window[i]=s[idx:idx+word_len]
                idx+=word_len
            if Counter(window)==word_count:
                res.append(low)
            # if window[0] in words : 
            #     if len(window)>1 and window[0]!=window[1]:
            #         low+=word_len
            #         high+=word_len
            #     else:
            #         low+=1
            #         high+=1
            # else:
            low+=1
            high+=1
        return res