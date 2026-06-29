from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cot = Counter(s)

        max_vowels = max(
            (amount for letter, amount in cot.items() if letter in vowels),
            default=0
        )

        max_consonants = max(
            (amount for letter, amount in cot.items() if letter not in vowels),
            default=0
        )

        return max_consonants + max_vowels
