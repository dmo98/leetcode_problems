from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # maintain a monotonically decreasing stack that stores elements in 'nums2' for which the next greater element hasn't been found. Iterate over 'nums2', if the current element is greater than the top of the stack, keep popping and set store this next greater element in a hashmap for O(1) access while building the answer from 'nums1'
        stack = []
        next_greater_element = defaultdict(int)
        for num in nums2:
            while (len(stack) != 0) and num > stack[-1]:
                value = stack.pop()
                next_greater_element[value] = num
                
            stack.append(num)
        
        # for remaining numbers on the stack, the next greater number is set to -1
        for num in stack:
            next_greater_element[num] = -1
        
        # build the answer from 'nums1'
        answer = []
        for num in nums1:
            answer.append(next_greater_element[num])
        return answer
        