class Solution:
    def isPalindrome(self, s: str) -> bool:
        last_index = len(s) - 1
        first_index = 0
        
        while first_index <= last_index:

            while not s[first_index].isalnum() :
                #print(s[first_index])
                first_index += 1 
                if first_index >= len(s) - 1:
                    break
            while not s[last_index].isalnum():
                #print(s[first_index])
                last_index -= 1 
                if last_index <= 0:
                    return True
            if s[first_index].upper() != s[last_index].upper():
                return False
            else: 
                first_index += 1 
                last_index -= 1 

        return True
