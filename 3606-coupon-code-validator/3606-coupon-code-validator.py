import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        electronics = []
        grocery = []
        pharmacy = []
        restaurant = []
        for i in range(len(code)):
            if isActive[i]:
                codd = code[i]
                if codd is not None and re.fullmatch(r"[a-zA-Z0-9_]+", codd):
                    line = businessLine[i]
                    if line == "electronics":
                        electronics.append(code[i])
                    elif line == "grocery":
                        grocery.append(code[i])
                    elif line == "pharmacy":
                        pharmacy.append(code[i])
                    elif line == "restaurant":
                        restaurant.append(code[i])
        
        electronics.sort()
        grocery.sort()
        pharmacy.sort()
        restaurant.sort()
        return electronics + grocery + pharmacy + restaurant