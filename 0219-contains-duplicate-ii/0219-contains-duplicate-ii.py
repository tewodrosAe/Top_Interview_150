class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = defaultdict(list)

        for i in range(len(nums)):
            n = nums[i]
            check = i - k
            if n in numDict:
                for a in numDict[n]:
                    if abs(a - i) <= k:
                        return True
            numDict[n].append(i)

        return False