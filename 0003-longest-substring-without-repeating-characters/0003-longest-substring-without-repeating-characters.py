class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxString = 0
        stringSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in stringSet:
                stringSet.remove(s[l])
                l += 1
            stringSet.add(s[r])
            maxString = max(maxString, r-l+1) 
        return maxString
            