# Last updated: 10/21/2025, 2:03:35 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        final = len(nums) - count
        for i in range(count):
            nums.remove(val)
        return final