class Solution:
    def residuePrefixes(self, s: str) -> int:
        unique = set()
        counter = 0
        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
            if (i+1) % 3 == len(unique):
                counter += 1
        return counter