class Solution(object):
    def stringprocess(self,s):
        stack=[]
        for ch in s:
            if ch=='#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=self.stringprocess(s)
        t=self.stringprocess(t)
        if s==t:
            return True
        else:
            return False
