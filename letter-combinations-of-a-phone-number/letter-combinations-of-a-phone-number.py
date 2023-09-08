class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach: Use backtracking. The helper function takes "curr" as the current combination being built. Base case -> combination reaches digits.length, append it to the answer array and return.
        
        letters = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        def backtrack(curr):
            if len(curr) == len(digits):
                # edge case: empty string passed in
                if digits == "":
                    return []
                answer.append("".join(curr))
                return
            
            next_digit = digits[len(curr)]
            for letter in letters[next_digit]:
                curr.append(letter)
                backtrack(curr)
                curr.pop()
                
        answer = []
        backtrack([])
        return answer
            
            
        