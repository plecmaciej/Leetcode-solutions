class Solution:
    def reverser(self, num: int) -> int:
        output = 0
        while num > 0:
            output = output * 2
            output += num % 2
            num = num // 2
        return output

    def sortByReflection(self, nums: List[int]) -> List[int]:
        values = []
        for num in nums:
            values.append((num, self.reverser(num)))
        return list(map(lambda p: p[0],sorted(values, key=lambda p: (p[1], p[0]))))
        