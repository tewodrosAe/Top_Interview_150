class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        current = []
        for num in sorted(intervals, key = lambda x:x[0]):
            if current == []:
                current = num
                continue
            if num[0] <= current[1]:
                current[1] = max(current[1], num[1])
            else:
                output.append(current)
                current = num
        
        return output + [current]