class Solution:
    def reverseWords(self, s: str) -> str:
        parts = s.split()
        parts.reverse()
        return " ".join(parts) 