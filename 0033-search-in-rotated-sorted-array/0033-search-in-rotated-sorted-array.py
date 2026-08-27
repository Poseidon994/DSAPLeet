class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1
        res=-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                return guess
            if nums[guess]>nums[n-1]:
                #Part1
                if nums[guess]<target:
                    low=guess+1
                else:
                    if target<nums[0]:
                        low=guess+1
                    else:
                        high=guess-1
                continue
            else:
                #Part2
                if nums[guess]>target:
                    high=guess-1
                else:
                    if target>nums[n-1]:
                        high=guess-1
                    else:
                        low=guess+1
                continue
        return -1