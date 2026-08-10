class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        res=[-1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            st.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop()
            if st:
                res[i]=st[-1]
            st.append(nums[i])
        return res