class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in sorted(intervals , key = lambda x:x[0]):
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1],result[-1][1])
            else:
                result.append(interval)
        return result 