class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen={'a':-1,'b':-1,'c':-1}
        count=0
        for right,ch in enumerate(s):
            last_seen[ch]=right
            count+=1+min(last_seen['a'],last_seen['b'],last_seen['c'])
        return count


        