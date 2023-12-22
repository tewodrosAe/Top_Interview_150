class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        roman = {
           'I': 1,
           'V': 5,
           'X':10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000 
        }
        add = 0
        for i in range(len(s)-1):
            if roman[s[i]] >= roman[s[i+1]]:
                add += roman[s[i]]
            else:
                add -= roman[s[i]]
        
        return add + roman[s[-1]]
            
            
            