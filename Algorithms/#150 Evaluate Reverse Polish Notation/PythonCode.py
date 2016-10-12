"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

"""

# It seems that -6 / 10 is supposed to be 0 instead of -1 


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        Stack = []
        
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                Stack.append(int(token))
            else:
                #print Stack
                val1 = Stack.pop()
                val2 = Stack.pop()
                if token == '*':
                    val = val2*val1
                elif token == '/':
                    val = abs(val2) / abs(val1) 
                    if val2 * val1 < 0:
                        val = val*(-1)
                    
                elif token == '+':
                    val = val2 + val1
                elif token == '-':
                    val = val2 - val1
                Stack.append(val)
                
        return Stack[-1]
        