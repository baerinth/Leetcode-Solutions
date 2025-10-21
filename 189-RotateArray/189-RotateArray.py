# Last updated: 10/21/2025, 2:03:17 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(k):
            y = nums.pop()
            nums.insert(0,y)