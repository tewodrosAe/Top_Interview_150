class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        length = len(nums)
        i = 0
        while i < length:
            current = [nums[i]]
            while i + 1 < length and nums[i] == nums[i+1] - 1:
                current.append(nums[i+1])
                i += 1
            if len(current) > 1:
                output.append(str(current[0]) +"->" +str(current[-1]))
            else:
                output.append(str(current[0]))
            i += 1
        return output