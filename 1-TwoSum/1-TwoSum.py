# Last updated: 10/21/2025, 2:03:49 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            try:
                if nums.index((target - x), nums.index(x) + 1) >= 0:
                    return [nums.index((target - x), nums.index(x) + 1), nums.index(x)]
            except ValueError:
                continue