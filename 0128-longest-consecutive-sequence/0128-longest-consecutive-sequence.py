class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest = 0
        numsSet = set(nums)
        
        for n in nums:
            if (n-1) not in numsSet:
                current = 1
                while n + current in numsSet:
                    current += 1
                highest = max(highest, current)
        
        return highest