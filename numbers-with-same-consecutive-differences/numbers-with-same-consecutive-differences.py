class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # Approach: Use backtracking. The helper function takes the current number being built as an argument, as well as the number of digits in it. Base case -> num.length == n, append to the answer array and return. For the first level in the tree, the choice of digits is 1->9, and for the other digits, we can choose from 0->9. Only consider paths where the difference between current and previous digits is k, otherwise abandon path / backtrack
        
        def backtrack(current_num, level):
            # base case
            if len(current_num) == n:
                number = int("".join(current_num))
                answer.append(number)
                return
            
            if level == 0:
                start = 1
            else:
                start = 0
                
            for digit in range(start, 10):
                if level == 0:  # no previous digit to compare to
                    current_num.append(str(digit))
                    backtrack(current_num, level+1)
                    current_num.pop()
                else: # only make recursive call if difference in digits is k
                    prev_digit = int(current_num[-1])
                    if abs(prev_digit - digit) == k:
                        current_num.append(str(digit))
                        backtrack(current_num, level+1)
                        current_num.pop()
                        
        answer = []
        backtrack([], 0)
        return answer
            
        
        