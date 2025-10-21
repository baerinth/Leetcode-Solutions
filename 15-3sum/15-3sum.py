# Last updated: 10/21/2025, 2:03:41 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        prev = 1000000
        while len(nums) > 2:
            l, r = 1, len(nums)-1
            if prev == nums[0]: 
                nums.pop(0)
                print("dupe")
                continue
            while l < r:
                s = nums[0] + nums[l] + nums[r]
                li = [nums[0], nums[l], nums[r]]
                lruntime, rruntime = nums[l], nums[r]
                if s == 0: 
                    a.append(li)
                    while l<r and nums[l] == lruntime: l+=1
                    while l<r and nums[r] == rruntime: r-=1
                elif s > 0: r-=1
                else: l+=1
            prev = nums[0]
            nums.pop(0)

        return a