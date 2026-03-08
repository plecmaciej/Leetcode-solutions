class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        dictionary = {}
        for letter in s:
            if letter in dictionary:
                dictionary[letter] +=1
            else:
                dictionary[letter] = 1
        frequency = {}
        for key, value in dictionary.items():
            if value not in frequency:
                frequency[value] =[]
            frequency[value].append(key)
        max_size = max(len(v) for v in frequency.values())
        candidates = [freq for freq, letters in frequency.items() if len(letters) == max_size]
        best_freq = max(candidates)

        return "".join(frequency[best_freq])