class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        length = len(nums)
        score = 0
        for i in range(k):
            bigger_then_prev = True
            prev_value = nums[i]
            #print("prev",prev_value)
            for j in range(i+k,length,k):
                current_value = nums[j]
                #print("curr",current_value)
                if bigger_then_prev:
                    #print("is bigger !!!")
                    if prev_value > current_value:
                        score += prev_value
                        bigger_then_prev = False
                        #print("is bigger and happy!!!")
                    elif prev_value == current_value:
                        bigger_then_prev = False
                elif prev_value >= current_value:
                    bigger_then_prev = False
                else:
                    bigger_then_prev = True
                
                prev_value = current_value

            if bigger_then_prev: 
                score += prev_value
                #print("is bigger and happy lst!!!")


        return score 