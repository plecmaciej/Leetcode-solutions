class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letter = 'y'
        result = ""
        min_number_of_letters = len(min(strs, key=len))
        for i in range(min_number_of_letters):
            letter = strs[0][i]
            if all(s[i] == letter for s in strs):
                result += letter
            else:
                return result
        return result