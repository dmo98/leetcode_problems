class Solution {
    public String restoreString(String s, int[] indices) {
        char[] shuffledString = new char[indices.length];
        for (int i = 0; i < indices.length; i++){
            shuffledString[indices[i]] = s.charAt(i);
        }
        String result = String.valueOf(shuffledString);
        return result;
    }
}