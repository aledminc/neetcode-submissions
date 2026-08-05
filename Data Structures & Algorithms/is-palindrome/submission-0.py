class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        for i,j in zip(s, s[::-1]):
            if i != j:
                return False
        return True