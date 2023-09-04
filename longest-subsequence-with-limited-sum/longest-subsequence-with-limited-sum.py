class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Approach: Sort nums and compute prefix sums (Pre-processing). Then, search for the index where we would insert queries[i] in the prefix sum array. That index is the number of elements on the left, which is also the maximum subsequence size whose sum is <= queries[i]
        
        # pre-process input
        nums.sort()
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])
            
        # main logic
        def binary_search(array, target):
            # return the index of the last occurrence of target (if present) + 1
            left = 0
            right = len(array)-1
            while left <= right:
                mid = (left + right)//2
                if array[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # left pointer will point at last occurrence of target + 1
            return left
        
        answer = []
        for query in queries:
            index = binary_search(prefix_sums, query)
            answer.append(index)
        return answer
        
        