class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(', '}':'{', ']':'['} # create a dictionary to map closing parentheses to opening parentheses. 
        stack = []  # initialize a stack to contain all unpaired parentheses
        for c in s:
            if c in parentheses.values(): # add all opening parentheses to stack
                stack.append(c)
            elif c in parentheses.keys():
                if len(stack) == 0: # Edge case: E.g. if s = '()]' or '}'. Needed because we can't access -1 index of an empty stack
                    return False
                if parentheses[c] == stack[-1]: # if a matching closing parentheses is found and it's valid (found at -1 index of stack), pop it's corresponding opening parentheses from stack
                    stack.pop()
                else: # if the closing parentheses doesn't match the last opening parentheses in stack, add it to stack. This will basically make sure that at the end, the stack won't be empty and False is returned
                    stack.append(c)
        return len(stack) == 0