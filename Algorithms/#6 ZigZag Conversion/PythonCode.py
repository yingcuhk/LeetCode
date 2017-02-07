"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        start = 0
        newS = ""
        L = len(s)
        if numRows == 1:
            return s

        if (L-numRows) % (2*numRows - 2) == 0:
            max_cols = (L-numRows) / (2*numRows - 2) + 1
        else:
            max_cols = (L-numRows) / (2*numRows - 2) + 2

        for row in range(numRows):
            for k in range(max_cols):
                pos = k*numRows + k*(numRows-2) + row
                if pos < L:
                    newS += s[pos]
                if row >0 and row < numRows-1:
                    pos2 = k*numRows + k*(numRows-2) + numRows + numRows-2-row
                    if pos2 < L:
                        newS += s[pos2]
    
        return newS
                
                
                