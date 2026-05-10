class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest_finish = 1000000
        land_num = len(landStartTime)
        water_num = len(waterStartTime)

        for i in range(land_num):
            step1 = landDuration[i] + landStartTime[i]

            for j in range(water_num):
                if waterStartTime[j] > step1:
                    finish = waterStartTime[j] + waterDuration[j]
                else:
                    finish = step1 + waterDuration[j]

                if finish < earliest_finish:
                    earliest_finish = finish
                #print(finish)
        
        for i in range(water_num):
            step1 = waterDuration[i] + waterStartTime[i]
            for j in range(land_num):
                if landStartTime[j] > step1:
                    finish = landStartTime[j] + landDuration[j]
                else:
                    finish = step1 + landDuration[j]
                if finish < earliest_finish:
                    earliest_finish = finish
                #print(finish)


        return earliest_finish