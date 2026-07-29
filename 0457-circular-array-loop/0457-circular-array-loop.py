class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)
        
        def next_index(i):
            return ((i + nums[i]) % n + n) % n
        
        def is_same_direction(i, j):
            return (nums[i] > 0 and nums[j] > 0) or (nums[i] < 0 and nums[j] < 0)
        
        for i in range(n):
            if nums[i] == 0:
                continue  # already proven invalid, skip
            
            slow, fast = i, i
            visited = []  # track every node touched in this attempt
            
            while True:
                # --- move slow one step ---
                prev_slow = slow
                slow = next_index(slow)
                visited.append(prev_slow)
                if not is_same_direction(prev_slow, slow):
                    break
                
                # --- move fast two steps, checking BOTH hops ---
                mid = next_index(fast)
                visited.append(fast)
                if not is_same_direction(fast, mid):
                    break
                
                new_fast = next_index(mid)
                visited.append(mid)
                if not is_same_direction(mid, new_fast):
                    break
                
                fast = new_fast
                
                # --- check for cycle ---
                if slow == fast:
                    if slow == next_index(slow):
                        break  # self-loop (length 1) — invalid
                    else:
                        return True  # real cycle found
            
            # this attempt failed — mark every node visited as dead
            for node in visited:
                nums[node] = 0
        
        return False