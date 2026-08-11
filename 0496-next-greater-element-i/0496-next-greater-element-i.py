class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st=[]
        res1=dict()
        res2=[-1]*len(nums1)
        st.append(nums2[len(nums2)-1])
        for i in range(len(nums2)-2,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if st:
                res1[nums2[i]]=res1.get(nums2[i],st[-1])
            st.append(nums2[i])
        for i in range(len(nums1)):
            res2[i]=res1.get(nums1[i],-1)
        return res2