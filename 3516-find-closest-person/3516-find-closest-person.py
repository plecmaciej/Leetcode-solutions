class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        ZX_dist = abs(z - x)
        ZY_dist = abs(z - y)
        if ZX_dist < ZY_dist:
            return 1
        elif ZX_dist > ZY_dist:
            return 2
        return 0