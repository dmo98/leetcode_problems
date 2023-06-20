class Solution:
    def countElements(self, arr: List[int]) -> int:
        distinct_nums = set(arr)
        result = 0
        for i in range(len(arr)):
            if arr[i]+1 in distinct_nums:
                result += 1
        return result