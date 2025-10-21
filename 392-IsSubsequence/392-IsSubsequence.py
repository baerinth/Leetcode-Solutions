# Last updated: 10/21/2025, 2:03:16 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for x in t:
            if i>=len(s): True
            elif x == s[i]: i+=1
        return i>=len(s)