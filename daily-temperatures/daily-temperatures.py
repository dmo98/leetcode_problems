class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # NEEDED HELP
        answer = [0]*len(temperatures)
        stack = [0] # initialize a stack that stores the indices of the temperatures for whom a warmer temperature hasn't been found on a later day yet
        # go through the 'temperatures' list. when you encounter an element thats greater than the last item in the stack, find the distance between their indices and store it in 'answer'. keep doing this for all the items in the stack less than the current element in 'temperatures'. also store the current element in stack to find the distance between it and the closest warmer day 
        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[stack[-1]]:
                while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    answer[index] = i - index

            stack.append(i)
        return answer
        
        