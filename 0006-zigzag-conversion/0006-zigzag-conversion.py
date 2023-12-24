class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        res = ''
        for i in range(numRows):
            if(i == 0 or i == numRows - 1):
                idx = i
                while idx < len(s):
                    res += s[idx]
                    idx += (numRows + (numRows - 2))
            else:
                idx = i
                while idx < len(s):
                    index = (idx + (numRows + (numRows - 2))) - (2*i)
                    res += s[idx]
                    if index < len(s):
                        res += s[index]
                    idx += (numRows + (numRows - 2))
        return res
                
                
                
        # n = len(numRows)
        # res = s[0]
        # cal = n + (n - 2)  ==> first and last row
        # n + (n - 2) 
        # 6 - 2(row) 
        # 1, 5
        # overallCal = cal - (i*((n-1)-i)) ==> rest of the row
        

        