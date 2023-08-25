class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # Approach: At each step, greedily choose the lightest apple, keeping track of the #apples and making sure that the total weight <= 5000
        
        ordered_weights = sorted(weight)
        
        num_apples = 0
        total_weight = 0
        for i in range(len(ordered_weights)):
            if total_weight + ordered_weights[i] <= 5000:
                total_weight += ordered_weights[i]
                num_apples += 1
            else:
                break
                
        return num_apples    
        