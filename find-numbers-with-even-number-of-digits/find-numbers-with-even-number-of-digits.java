class Solution {
    public int findNumbers(int[] nums) {
        int numEvenDigits = 0;
        for (int i = 0; i < nums.length; i++) {
            if (String.valueOf(nums[i]).length() % 2 == 0) {
                numEvenDigits += 1;
            }
            // if (numDigits(nums[i]) % 2 == 0) {
            //     numEvenDigits += 1;
            // }
        }
        
        return numEvenDigits;
    }
    
//     public int numDigits(int num) {
//         int digits = 0;
        
//         while (num >= 1) {
//             num = Math.floorDiv(num, 10);
//             digits += 1;
//         }
        
//         // System.out.println(digits);
//         return digits;
//     }
}