# Last updated: 10/21/2025, 2:03:46 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s = list(s)
        order = list(range(1,numRows+1))
        intermediate = list(range(1,numRows+1))
        intermediate.remove(1)
        if intermediate:
            intermediate.pop()
        intermediate = intermediate[::-1]
        order = order + intermediate
        zigzag = [[] * 7 for i in range(numRows)]
        while len(s) > 0:
            zigzag[order[0]-1].append(s[0])
            s.pop(0)
            order.append(order.pop(0))
        output = ''
        for x in zigzag:
            output += ''.join(x)
        return output

