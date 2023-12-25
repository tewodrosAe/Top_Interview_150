class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0
        
        for i in range(len(haystack) - (len(needle) - 1)):
            j = 0
            while needle[j] == haystack[i + j]:
                j += 1
                if j >= len(needle):
                    return i
            
            
        return -1