# Last updated: 10/21/2025, 2:03:36 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for x in range(len(nums)):
            if x > 0:
                if nums[x-count] == nums[x-(1+count)]:
                    nums.pop(x-count)
                    count+=1