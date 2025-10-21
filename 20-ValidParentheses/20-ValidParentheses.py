# Last updated: 10/21/2025, 2:03:38 PM
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        dic = {"(":")","[":"]","{":"}"}
        for x in s:
            if x in dic: 
                stack.append(dic.get(x))
                continue
            if len(stack) != 0 and stack[-1] == x: stack.pop()
            else: return False
        return len(stack) == 0

