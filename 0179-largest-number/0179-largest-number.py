class Solution:

    def compare_numbers(self, num1: int, num2: int):
        str_num1 = str(num1)
        str_num2 = str(num2)

        if str_num1 + str_num2 > str_num2 + str_num1:
            return num1
        else:
            return num2

    def merge_sort(self, lista: List[int]):
        if len(lista) < 2:
            return lista

        middle = len(lista) // 2
        left_half = self.merge_sort(lista[:middle])
        right_half = self.merge_sort(lista[middle:])

        return self.merge(left_half, right_half)

    def merge(self, left: List[int], right: List[int]):
        wynik = []
        i = j = 0

        while i < len(left) and j < len(right):
            if self.compare_numbers(left[i], right[j]) == left[i]:
                wynik.append(left[i])
                i += 1
            else:
                wynik.append(right[j])
                j += 1

        wynik.extend(left[i:])
        wynik.extend(right[j:])

        return wynik

    def largestNumber(self, nums: List[int]) -> str:
        output = ""
        nums = self.merge_sort(nums)
        for i in range(len(nums)):
            output = output + str(nums[i])
        if len(output)> 1 and output[0] == '0':
            return "0"
        return output