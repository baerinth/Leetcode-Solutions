# Last updated: 10/21/2025, 2:03:20 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        output = ""
        for x in s:
            output += x
            output += " "
        output = output[:-1]
        return output