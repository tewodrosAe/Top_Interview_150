class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i < len(citations):
            if citations[i] <= i:
                break
            i += 1
        return i;