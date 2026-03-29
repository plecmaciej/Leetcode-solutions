class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        fastest = test = float("inf")
        for task in tasks:
            finish_time = task[0] + task[1]
            if finish_time < fastest:
                fastest = finish_time
        return fastest

