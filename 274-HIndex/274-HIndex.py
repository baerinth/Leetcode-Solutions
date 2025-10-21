# Last updated: 10/21/2025, 2:03:12 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        for x in range(len(citations)):
            if(x+1 > citations[x]):
                return x
        return len(citations)