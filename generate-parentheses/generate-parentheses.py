class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach: Use backtracking. The helper function takes the current string being built (as a list) and a stack (to determine if the parentheses are valid) as arguments. Base case -> len(parentheses) = 2*n, then append to the answer array.
        
        def backtrack(parentheses, stack):
            if len(parentheses) == 2*n and stack == []:
                answer.append("".join(parentheses))
                return 
            
            for next_char in ['(', ')']:
                if parentheses.count(next_char) + 1 > n: # valid parentheses can't be formed
                    continue
                
                if next_char == '(':
                    stack.append(next_char)
                elif next_char == ')':
                    if len(stack) > 0:
                        if stack[-1] == '(':
                            stack.pop()
                        else: # no opening parenthese to match closing, not valid
                            continue
                    else:
                        continue
                        
                parentheses.append(next_char)
                backtrack(parentheses, stack)
                # backtracking
                if parentheses[-1] == '(':
                    stack.pop()
                elif parentheses[-1] ==')':
                    stack.append('(')
                parentheses.pop()
                        
                
        answer = []
        backtrack([], [])
        return answer
        