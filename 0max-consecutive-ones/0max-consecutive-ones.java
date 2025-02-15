class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int numOnes = 0;
        int maxNumOnes = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                numOnes += 1;
            }
            else {
                numOnes = 0;
            }
            maxNumOnes = Math.max(numOnes, maxNumOnes);
        }
        return maxNumOnes;
    }
}