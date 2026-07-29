class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)
        
        def next_index(i):
            return ((i+nums[i])%n+n)%n
            pass
        
        def is_same_direction(i, j):
            return True if (nums[i]>0 and nums[j]>0) or (nums[i]<0 and nums[j]<0) else False
            pass
        
        for i in range(n):
            if nums[i] == 0:
                continue  # already marked invalid
            
            slow, fast = i, i
            
            while True:
                
                slow=next_index(slow)
                if  not is_same_direction(slow, next_index(slow)):
                    nums[slow]=0
                    break
                fast=next_index(next_index(fast))
                if not is_same_direction(fast,next_index(fast)) or not is_same_direction(next_index(fast),next_index(next_index(fast))):
                    nums[fast]=0
                    break
                if slow == fast:
                    break  
            
           
            if slow==fast and fast!=next_index(slow):
                return True
        
        return False