class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            increment = 2 * (numRows-1)
            for i in range(r,len(s),increment): # we start from r because row one will start at index one and row two will start at index two etc...
                res += s[i] # this will work for the first and last row only
                if (r>0 and r < numRows-1 and i+increment-2*r<len(s)): # if we at a middle row 
                    res+=s[i+increment-2*r]
        return res 