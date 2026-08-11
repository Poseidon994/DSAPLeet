class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[]
        res=[0]*len(temperatures)
        res[len(temperatures)-1]=0
        st.append(len(temperatures)-1)
        for i in range(len(temperatures)-2,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if st:
                res[i]=st[-1]-i
            st.append(i)
        return res