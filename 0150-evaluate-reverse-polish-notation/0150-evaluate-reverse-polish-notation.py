class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_nums = []
        right_num = 0
        for token in tokens:
            if token == '+':
                right_num = stack_nums.pop()
                stack_nums.append(stack_nums.pop() + right_num)
            elif token == '-':
                right_num = stack_nums.pop()
                stack_nums.append(stack_nums.pop() - right_num)
            elif token == '*':
                right_num = stack_nums.pop()
                stack_nums.append(stack_nums.pop() * right_num)
            elif token == '/':
                right_num = stack_nums.pop()
                stack_nums.append(int(stack_nums.pop() / right_num))    
            else:
                stack_nums.append(int(token))
            #print(stack_nums)

        return stack_nums[-1]
            