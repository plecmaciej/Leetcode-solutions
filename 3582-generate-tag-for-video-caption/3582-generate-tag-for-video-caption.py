class Solution:
    def generateTag(self, caption: str) -> str:
        output = []
        output.append('#')

        length = len(caption)
        i = 0

        while i < length:
            if caption[i].isalpha():
                output.append(caption[i].lower())
                i+=1
                break
            i+=1

        while i < length and len(output) <= 99:
            if caption[i] == ' ':
                if (i + 1) < length:
                    if caption[i+1].isalpha():
                        output.append(caption[i+1].upper())
                        i += 1
            else: 
                output.append(caption[i].lower())
            i += 1
        
        
        output = "".join(output)
        return output