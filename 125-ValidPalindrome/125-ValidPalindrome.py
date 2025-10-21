# Last updated: 10/21/2025, 2:03:22 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        return s == s[::-1]