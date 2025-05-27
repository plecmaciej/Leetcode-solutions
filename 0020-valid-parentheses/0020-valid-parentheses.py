class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ('(','{','['):
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    toper = stack.pop()
                    if s[i] == ')' and toper !='(' :
                        return False
                    elif s[i] == '}' and toper !='{' :
                        return False
                    elif s[i] == ']' and toper !='[' :
                        return False    
                else:
                    return False 
        if len(stack) == 0:
            return True
        else:
            return False 