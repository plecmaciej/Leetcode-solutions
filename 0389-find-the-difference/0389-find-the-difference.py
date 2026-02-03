class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for letter, count in counter2.items():
            #print(letter, count)
            if counter1[letter] < count:
                return letter