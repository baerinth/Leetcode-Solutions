# Last updated: 10/21/2025, 2:03:32 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        target = 0
        for x in range(1,len(nums)):
            if((x-target) - nums[x] <= 0):
                target = x

        return (target == len(nums) - 1)
