class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = len(strs[0])
        
        for i in range(len(strs)):
            minLen = min(minLen, len(strs[i]))
            
        res = ''
        
        for i in range(minLen):
            s = strs[0][i]
            for j in range(len(strs)):
                if s != strs[j][i]:
                    return res
            res += s
        return res