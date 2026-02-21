class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = "Fizz"
        buzz = "Buzz"
        output_list = []
        for i in range(1,n + 1):
            word_in_list = ""
            if i % 3 == 0:
                word_in_list = fizz
                if i % 5 == 0:
                    word_in_list = word_in_list + buzz
            elif i % 5 == 0:
                word_in_list = buzz
            else:
                word_in_list = str(i)
            output_list.append(word_in_list)

        return output_list

