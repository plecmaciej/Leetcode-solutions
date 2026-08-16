class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        skipped_baskets = []
        last_basket = 0
        is_skipped = False
        is_found = False
        unplaced = 0

        for fruit in fruits:
            #print("new fruit ", fruit)
            for skipped in skipped_baskets:
                #print(1)
                if baskets[skipped] >= fruit:
                    #print(2)
                    skipped_baskets.remove(skipped)
                    is_skipped = True
                    break

            if is_skipped:
                #print(3)
                is_skipped = False
            else:
                for i in range(last_basket , len(baskets)):

                    #print(4, last_basket, "ostatni")
                    last_basket = i + 1
                    if baskets[i] >= fruit:
                        #print(5)
                        is_found = True
                        break
                    else:
                        skipped_baskets.append(i)
                
                if is_found:
                    #print(6)
                    is_found = False
                else:
                    #print(7)
                    unplaced +=1
            
        
        return unplaced