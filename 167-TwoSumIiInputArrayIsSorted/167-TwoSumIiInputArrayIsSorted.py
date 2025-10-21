# Last updated: 10/21/2025, 2:03:19 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target: return [i+1,j+1]
            if numbers[i] + numbers[j] > target: j-=1 
            else: i+=1