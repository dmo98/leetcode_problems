class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Approach: At each step, greedily load the box containing the most #units onto the truck, keeping count of the total #units and making sure that the number of boxes <= truckSize.
        
        ordered_boxes = sorted(boxTypes, key = lambda box:box[1], reverse=True)
        
        total_units = 0
        for i in range(len(ordered_boxes)):
            if truckSize <= 0:
                break
            
            while truckSize > 0:
                if ordered_boxes[i][0] > 0:
                    total_units += ordered_boxes[i][1]
                    ordered_boxes[i][0] -= 1
                    
                    truckSize -= 1
                else:
                    break
                    
        return total_units
        