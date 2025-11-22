class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_of_patterns = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map_of_patterns:
                map_of_patterns[pattern[i]] = words[i]
            else:
                if map_of_patterns[pattern[i]] != words[i]:
                    return False
        values = list(map_of_patterns.values())
        unique = set(values)

        if len(values) == len(unique):
            return True
        else:
            return False 