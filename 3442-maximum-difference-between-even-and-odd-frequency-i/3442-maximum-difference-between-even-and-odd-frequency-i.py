from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        licznik = Counter(s)
        hi_odd = 0
        lo_eve = 101
        for sign in licznik:
            #print(sign)

            if licznik[sign] % 2 == 1 and hi_odd < licznik[sign]:
                hi_odd = licznik[sign]
                #print(sign, licznik[sign], "1ww")

            elif licznik[sign] % 2 == 0 and lo_eve > licznik[sign]:
                lo_eve = licznik[sign]
                #print(sign, licznik[sign], "2ww")

        
        return hi_odd - lo_eve