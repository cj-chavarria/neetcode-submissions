class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
        return s_list == list(reversed(s_list))

        