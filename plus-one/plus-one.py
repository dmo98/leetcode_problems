class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # compute the number
        value = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            power_of_ten = n-1-i
            digit = digits[i]
            value += (10 ** power_of_ten) * digit
        
        value += 1
        result = []
        while value > 0:
            result.insert(0, value % 10)
            value //= 10
        return result
            
        