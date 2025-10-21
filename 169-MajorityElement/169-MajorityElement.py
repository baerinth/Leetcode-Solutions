# Last updated: 10/21/2025, 2:03:18 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = len(nums) // 2
        for x in nums:
            count[x] +=1

        for x, y in count.items():
            if y > n:
                return x