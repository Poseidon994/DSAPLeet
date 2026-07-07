class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i]<0:
                a.append(nums[i]*nums[i])
            else:
                b.append(nums[i]*nums[i])
        
        if len(a)==0:
            return b
        elif len(b)==0:
            return a[::-1]
        else:
            a=a[::-1]
            i=0
            j=0
            idx=0
            while i<len(a) and j<len(b):
                if a[i]<=b[j]:
                    nums[idx]=a[i]
                    i+=1
                else:
                    nums[idx]=b[j]
                    j+=1
                idx+=1
            while i<len(a):
                nums[idx]=a[i]
                i+=1   
                idx+=1
            while j<len(b):
                nums[idx]=b[j]
                j+=1
                idx+=1
            return nums