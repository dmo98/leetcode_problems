import math

def RPN(tokens):
    if tokens[2] == '+':
        return tokens[0]+tokens[1]
    elif tokens[2] == '-':
        return tokens[0]-tokens[1]
    elif tokens[2] == '*':
        return tokens[0]*tokens[1]
    elif tokens[2] == '/':
        answer = tokens[0]/tokens[1]
        if answer > 0:
            return math.floor(answer)
        else:
            return math.ceil(answer)
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in '+-*/':
                stack.append(int(tokens[i]))
            else:
                answer = RPN(stack[-2:]+[tokens[i]])
                for _ in range(2):
                    stack.pop()
                stack.append(answer)
            #print(stack)
        return stack[0]