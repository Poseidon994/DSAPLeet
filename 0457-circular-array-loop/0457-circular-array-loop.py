class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)
        
        def next_index(i):
            return ((i + nums[i]) % n + n) % n
        
        def is_same_direction(i, j):
            return (nums[i] > 0 and nums[j] > 0) or (nums[i] < 0 and nums[j] < 0)
        
        for i in range(n):
            if nums[i] == 0:
                continue  
            
            slow, fast = i, i
            visited = [] 
            
            while True:
                prev_slow = slow
                slow = next_index(slow)
                visited.append(prev_slow)
                if not is_same_direction(prev_slow, slow):
                    break
                
                mid = next_index(fast)
                visited.append(fast)
                if not is_same_direction(fast, mid):
                    break
                
                new_fast = next_index(mid)
                visited.append(mid)
                if not is_same_direction(mid, new_fast):
                    break
                
                fast = new_fast
                if slow == fast:
                    if slow == next_index(slow):
                        break  
                    else:
                        return True 
            
            for node in visited:
                nums[node] = 0
        
        return False