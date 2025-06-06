class Solution:
    def addBinary(self, a: str, b: str) -> str:
        additional = '0'
        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        diff = len(longer) - len(shorter)

        counter = len(shorter) - 1
        while counter >=0:
            if longer[counter+diff] == '1' and shorter[counter] == '1':
                longer = longer[:counter+diff] + additional + longer[counter+diff+1:]
                additional = '1'
            elif longer[counter+diff] == '0' and shorter[counter] == '0':
                longer = longer[:counter+diff] + additional + longer[counter+diff+1:]
                additional = '0'
            else:
                if additional == '0':
                    longer = longer[:counter+diff] + '1' + longer[counter+diff+1:]
                else:
                    longer = longer[:counter+diff] + '0' + longer[counter+diff+1:]
                    additional = '1'
            counter = counter - 1
        diff = diff - 1
        while diff > 0:
            if additional == '0':
                return longer
            else:
                if longer[diff] == '0':
                    longer = longer[:diff] + '1' + longer[diff+1:]
                    return longer
                else:
                    longer = longer[:diff] + '0' + longer[diff+1:]
            diff = diff - 1
        if additional == '1':
            if diff < 0:
                longer = additional + longer
            else:
                longer = "10" + longer[1:]
        return longer