# Last updated: 10/21/2025, 2:03:42 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for x in range(1,len(strs[0])+1):
            for y in strs:
                if not (strs[0][:x] in y[:x]):
                    return output
            output = strs[0][:x]
        return output
            