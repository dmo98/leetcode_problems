from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n*2) time, O(n) space
        # Looked at NeetCode's solution code
        nums.sort()
        
        triplets = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  # avoid duplicates
                continue
                
            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = nums[left] + nums[right] + num
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    triplets.append([nums[left], nums[right], num])
                    
                    # continue search for other potential three sums with the same first number
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return triplets
        
#         # O(n*2) time, O(n) space -> Time Limit Exceeded (312/312 passed)
#         hashmap = defaultdict(list)
#         for i in range(len(nums)):
#             hashmap[nums[i]].append(i)
            
#         triplets = set()
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if -(nums[i] + nums[j]) in hashmap:
#                     indices = hashmap[-(nums[i] + nums[j])]
#                     for index in indices:
#                         if index != i and index != j:
#                             triplets.add(tuple(sorted([nums[i], nums[j], nums[index]])))
#                             break   # don't want to add duplicates
          
#         return [list(tup) for tup in triplets]
                            
        