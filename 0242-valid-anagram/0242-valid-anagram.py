class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        licznik1 = Counter(list(s))
        licznik2 = Counter(list(t))
        wspolne_elementy = licznik1 & licznik2
        liczba_wspolnych_elementow = sum(wspolne_elementy.values())
        if liczba_wspolnych_elementow != len(s) or liczba_wspolnych_elementow != len(t):
            return False
        else:
            return True 