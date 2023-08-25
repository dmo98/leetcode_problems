class Solution:
    def maximum69Number (self, num: int) -> int:
        # Approach: Iterate over the digits, swap the first '6' with a '9'
        digits = list(str(num))
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break
                
        return int("".join(digits))
        