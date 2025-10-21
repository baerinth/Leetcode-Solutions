# Last updated: 10/21/2025, 2:03:13 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        leftside = 1
        for x in range(len(nums)):
            answer[x] *= leftside
            leftside *= nums[x]

        rightside = 1
        for x in range(len(nums) - 1, -1, -1):
            answer[x] *= rightside
            rightside *= nums[x]
        
        return answer