class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break                          # can't sum to 0 anymore
            if i > 0 and nums[i] == nums[i-1]:
                continue                       # skip duplicate anchor

            low, high = i + 1, n - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1                # skip duplicate low
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1                # skip duplicate high
                elif total < 0:
                    low += 1
                else:
                    high -= 1

        return res
                


