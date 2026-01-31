class Solution:
    def firstUniqChar(self, s: str) -> int:
        wystapienia = {}

        for i in range(len(s)):
            if s[i] in wystapienia:
                wystapienia[s[i]].append(i)
            else:
                wystapienia[s[i]] = [i]
        for klucz, indeksy in wystapienia.items():
            if len(indeksy) == 1:
                return indeksy[0]
        return -1