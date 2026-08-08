class Solution(object):
    def maxNumberOfBalloons(self, text):

        a = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for ch in text:
            if ch in a:
                a[ch] += 1
        return min(a['b'], a['a'], a['n'], a['l']//2, a['o']//2)