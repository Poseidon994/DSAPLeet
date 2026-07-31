class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nodelete=arr[0]
        onedelete=float('-inf')
        ans=arr[0]
        for i in range(1,len(arr)):
            prevnodelete=nodelete
            prevonedelete=onedelete
            nodelete=max(arr[i],arr[i]+nodelete)
            if prevonedelete==float('-inf'):
                v2=arr[i]
            else:
                v2=arr[i]+prevonedelete
            onedelete=max(v2, prevnodelete)
            ans=max(ans,nodelete,onedelete)
        return ans
        