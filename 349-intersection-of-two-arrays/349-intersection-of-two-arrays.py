class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = {}
        counts2 = {}
        for i in range(len(nums1)):
            if nums1[i] not in counts1:
                counts1[nums1[i]] = 0
            counts1[nums1[i]] += 1
        
        for j in range(len(nums2)):
            if nums2[j] not in counts2:
                counts2[nums2[j]] = 0
            counts2[nums2[j]] += 1
            
        result = []
        for num in counts1.keys():
            if num in counts2.keys():
                result.append(num)
        
        return result