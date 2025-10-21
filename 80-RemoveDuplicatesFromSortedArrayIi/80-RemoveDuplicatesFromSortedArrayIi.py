# Last updated: 10/21/2025, 2:03:28 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        dup = 0
        for x in range(len(nums)):
            if x > 0:
                if nums[x-count] == nums[x-(1+count)]:
                    if dup >= 1:
                        nums.pop(x-count)
                        count+=1
                    else:
                        dup+=1
                else:
                    dup=0
                    