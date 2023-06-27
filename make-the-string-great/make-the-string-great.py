class Solution:
    def makeGood(self, s: str) -> str:
        # maintain a stack, if you encounter a different case letter to the letter at the top of the stack, pop the latter, else keep pushing to the stack
        stack = []
        for c in s:
            if stack != [] and (c != stack[-1] and c.lower() == stack[-1].lower()):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
            