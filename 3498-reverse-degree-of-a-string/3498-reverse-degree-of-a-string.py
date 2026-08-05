class Solution:
    def reverseDegree(self, s: str) -> int:
        VALUE_TO_SUB = 97 + 26
        summary = 0 
        for i in range(len(s)):
            summary += (VALUE_TO_SUB - ord(s[i])) * (i + 1)
        return summary