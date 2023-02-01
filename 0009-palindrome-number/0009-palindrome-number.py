class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] if x >= 0 else False