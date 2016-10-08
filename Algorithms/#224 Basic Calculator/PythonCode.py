"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        Stack = []
        
        substr = s
        
        count = 0 
        while len(substr) > 0:
            while len(substr) > 0 and substr[0] == ' ':
                substr = substr[1:]
            if len(substr) == 0:
                break
        
            char = substr[0]
            if char  == '(' or char == ')' or char == "+" or char == "-":
                val = char
                substr = substr[1:]
            else:
                
                val = 0
                remains = False
                for k, char in enumerate(substr):
                    if not char.isdigit():
                        remains = True
                        break
                    val = val*10 + int(char)
                if remains:
                    substr = substr[k:]
                else:
                    substr = substr[k+1:]
            
            #val, substr = self.next_num(substr)
            if len(str(val)) == 0:
                continue
            if val == "(" or val == "+" or val == "-":
                Stack.append(val)
            elif val == ")":
                val = Stack.pop()
                Stack.pop()
                while Stack and Stack[-1] != "(":
                    sig = Stack.pop()
                    newval = Stack.pop()
                    if sig == '-':
                        val = newval - val
                    elif sig == '+':
                        val = newval + val
                Stack.append(val)
            else:
                """
                if not Stack:
                    Stack.append(val)
                """
                while Stack and Stack[-1] != "(":
                    #print val
                    #print Stack
                    sig = Stack.pop()
                    newval = Stack.pop()
                    if sig == '-':
                        val = newval - val
                    elif sig == '+':
                        val = newval + val
                Stack.append(val)
            
        return Stack[-1]
           
            
     
        
        