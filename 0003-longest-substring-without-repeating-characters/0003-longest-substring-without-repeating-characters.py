class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxString = 1
        stringList = []
        l,r = 0,0
        while r < len(s):
            if s[r] in stringList:
                maxString = max(maxString, r-l)
                while s[r] in stringList:
                    stringList.pop(0)
                    l += 1
            stringList.append(s[r])
            r += 1
        maxString = max(maxString, r-l)    
        return maxString
            