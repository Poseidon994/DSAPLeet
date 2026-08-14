class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st=[]
        pair=[]
        for i in range(len(s)):
            c=s[i]
            if not st:
                st.append([s[i],1])
                continue
            if st and st[-1][0]!=c:
                st.append([c,1])
                continue
            if st and st[-1][1]<k-1:
                pair=st[-1]
                st.pop()
                st.append([pair[0],pair[1]+1])
                continue
            st.pop()
        res=''
        while st:
            p=st[-1]
            st.pop()
            while p[1]:
                res+=p[0]
                p[1]-=1
        return res[::-1]