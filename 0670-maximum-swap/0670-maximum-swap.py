class Solution:
    def maximumSwap(self, num: int) -> int:
        # Approach: Obtain the list of digits. Store the digit : [indices where the digit occurs] in a hashmap. Iterate over the digits, if this digit is the maxDigit remaining in the hashmap, then delete it's entry in the hashmap, otherwise get the right-most index of the largest digit, and use it to swap with the integer at the current digit.
        
        digits = list(str(num))
        
        # build hashmap
        hashmap = {}
        for i in range(len(digits)):
            if digits[i] not in hashmap:
                hashmap[digits[i]] = [i]
            else:
                hashmap[digits[i]].append(i)
                
        # iterate over digits, checking if it's the max remaining, else swap
        for i in range(len(digits)):
            max_remaining = max(hashmap.keys())
            if digits[i] == max_remaining:
                # delete entry from hashmap (at that index if there are multiple occurrences)
                hashmap[digits[i]].pop(0)
                if hashmap[digits[i]] == []:
                    del hashmap[digits[i]]
            
            else:
                # get the right-most index of the max-remaining and swap
                right_most_index = hashmap[max_remaining][-1]
                
                
                temp = digits[i]
                digits[i] = digits[right_most_index]
                digits[right_most_index] = temp
                
                return int("".join(digits))
                
        # if all digits were in order
        return int("".join(digits))
        
        
                        