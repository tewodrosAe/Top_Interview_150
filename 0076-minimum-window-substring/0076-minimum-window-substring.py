class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case 
        if len(s) < len(t) or t == '':
            return ""
        
        # variables
        res, resLen = [-1,-1], len(s) + 1
        tDict = {}
        l = 0
        temp = {}  
        count = 0
        
        for char in t:
            tDict[char] = tDict.get(char,0) + 1
         
        for r in range(len(s)):
            c = s[r]
            temp[c] = temp.get(c,0) + 1
            
            if c in tDict and temp[c] == tDict[c]:
                count += 1
            
            while count == len(tDict):
                if resLen > r - l + 1:
                    res = [l, r+1]
                    resLen = r - l + 1
                temp[s[l]] -= 1
                if s[l] in tDict and tDict[s[l]] > temp[s[l]]:
                    count -= 1
                l += 1
            
        return s[res[0]: res[1]]
            