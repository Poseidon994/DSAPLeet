class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st=[]
        tokens=path.split('/')
        for i in tokens:
            if i=='' or i=='.':
                continue
            if i=='..':
                if st:
                    st.pop()
                    continue
            else:
                st.append(i)
        return '/'+'/'.join(st)