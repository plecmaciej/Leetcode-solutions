class Solution:
    def reverseVowels(self, s: str) -> str:
        list_from_str = list(s)
        vowels  = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = len(list_from_str) - 1 
        while left < right:
            while left < len(list_from_str) and list_from_str[left] not in vowels:
                left += 1
            while right >= 0 and list_from_str[right] not in vowels:
                right -= 1
        
            if left < right:
                list_from_str[left], list_from_str[right] = list_from_str[right], list_from_str[left]
                left += 1
                right -= 1
        return ''.join(list_from_str)