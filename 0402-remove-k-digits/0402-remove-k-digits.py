class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st=[]
        st.append(num[0])
        for i in range (1,len(num)):
            while st and k>0 and int(num[i])<int(st[-1]):
                st.pop()
                k-=1
            
            st.append(num[i])
        if k: 
            st = st[:-k]
        r=''.join(st)
        r=r.lstrip('0')
        if r:
            return r
        else: 
            return '0'
        