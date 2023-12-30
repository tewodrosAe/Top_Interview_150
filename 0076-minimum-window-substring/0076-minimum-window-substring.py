class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case 
        if t == '' or len(t) > len(s):
            return ''
        
        window, substring = {}, {}
        l = 0
        for w in t:
            substring[w] = substring.get(w,0) + 1  
        counter, subLength = 0, len(substring)
        res, resLength = [-1,-1], len(s) + 1 
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            
            if c in substring and substring[c] == window[c]:
                counter += 1
            
            while counter == subLength:
                window[s[l]] -= 1
                if r - l + 1 < resLength:
                    resLength = r - l + 1
                    res = [l, r+1]
                if s[l] in substring and window[s[l]] < substring[s[l]]:
                    counter -= 1
                l += 1 
            
        return s[res[0]: res[1]]