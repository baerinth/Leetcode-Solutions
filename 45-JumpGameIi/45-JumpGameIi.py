# Last updated: 10/21/2025, 2:03:33 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        nums.reverse()
        target = 0
        count = 0
        jump = 0
        while target != len(nums)-1:
            for x in range(target,len(nums)):
                if((x-target) - nums[x] <= 0):
                    jump = x
            count += 1
            target = jump
        return count
