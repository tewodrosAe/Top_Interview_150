class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        prev = []
        count = 0
        for p in sorted(points , key = lambda x:x[0]):
            if prev == []:
                prev = p
                continue
            if p[0] > prev[1]:
                count += 1
                prev = p
            else:
                prev = [prev[0], min(p[1],prev[1])]
        
        return count + 1