class Solution(object):
    def maxNumberOfBalloons(self, text):
        have=dict()
        for i in text:
            have[i]=have.get(i,0)+1
        need = {'b':1,'a':1,'l':2,'o':2,'n':1}
        res=float('inf')
        for char,val in need.items() :
            times=have.get(char,0)//need[char]
            res=min(res,times)
        return res