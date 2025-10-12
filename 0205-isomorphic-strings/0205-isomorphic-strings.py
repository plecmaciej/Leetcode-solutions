class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters_dictionary = {}
        for i in range(len(s)):
            if s[i] not in letters_dictionary:
                for key, value in letters_dictionary.items():
                    if value == t[i]:
                        return False
                letters_dictionary[s[i]] = t[i]
            elif letters_dictionary[s[i]] != t[i]:
                return False
        return True