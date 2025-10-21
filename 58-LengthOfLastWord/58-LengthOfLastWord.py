# Last updated: 10/21/2025, 2:03:31 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        count = 0
        for x in s:
            if x == " " and count > 0:
                return count
            elif x != " ":
                count += 1
        return count