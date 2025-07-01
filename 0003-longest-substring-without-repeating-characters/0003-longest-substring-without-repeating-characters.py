class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        counter = 0
        first_in_sequence = None
        letters_position = {}
        if len(s) == 0:
            return 0
        longest = 1
        counter = 1
        first_in_sequence = s[0]
        letters_position = {}
        letters_position[s[0]] = 0

        for i, letter in enumerate(s[1:], start=1):
            if letter not in letters_position:
                letters_position[letter] = i
                counter += 1
            else:
                if letter != first_in_sequence:
                    to_delete = [key for key, value in letters_position.items() if value < letters_position[letter]]
                    for key in to_delete:
                        del letters_position[key]  
                    if longest < counter:
                        longest = counter 
                    counter = len(letters_position)  

                if letters_position[letter] != i - 1:
                    for lettt, index in letters_position.items():
                        if index == letters_position[letter]+1:
                            first_in_sequence = lettt
                else:
                    first_in_sequence = letter

                letters_position[letter] = i
            #print(i, letter, counter, first_in_sequence, longest)
        
        if counter > longest:
            longest = counter 
        return longest