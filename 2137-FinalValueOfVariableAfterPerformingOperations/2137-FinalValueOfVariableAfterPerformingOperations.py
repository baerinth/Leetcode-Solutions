# Last updated: 10/21/2025, 2:03:11 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        y=0
        for x in operations:
            if x[1] == "+": y+=1
            else: y-=1
        return y