class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()

        if not words:
            return "#"

        result = "#" + words[0].lower()

        for word in words[1:]:
            result += word.capitalize()
            if len(result) > 100:
                break

        return result[0:100]