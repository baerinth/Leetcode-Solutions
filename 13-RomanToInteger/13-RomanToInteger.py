# Last updated: 10/21/2025, 2:03:43 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        prev = 1
        curr = 1
        output = 0
        for x in s:
            match x:
                case 'I':
                    curr=1
                case 'V':
                    curr=5
                case 'X':
                    curr=10
                case 'L':
                    curr=50
                case 'C':
                    curr=100
                case 'D':
                    curr=500
                case 'M':
                    curr=1000
            if (curr<prev):
                output -= curr
            else:
                output += curr
            prev = curr
        return output
            