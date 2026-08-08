class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        have=dict()
        need=dict()
        for i in ransomNote:
            need[i]=need.get(i,0)+1
        for i in magazine:
            have[i]=have.get(i,0)+1
        for char,val in need.items():
            if have.get(char,0)<need[char]:
                return False
        return True