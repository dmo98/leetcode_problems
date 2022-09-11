class Solution {
    public String restoreString(String s, int[] indices) {
        // creating a char array to store the individual characters at the correct           // indices
        char[] shuffledString = new char[indices.length];
        for (int i = 0; i < indices.length; i++){
            shuffledString[indices[i]] = s.charAt(i);
        }
        // convert char array to String
        String result = String.valueOf(shuffledString);
        return result;
    }
}