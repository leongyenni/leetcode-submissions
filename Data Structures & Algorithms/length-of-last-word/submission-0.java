class Solution {
    public int lengthOfLastWord(String s) {
        String[] sList = s.split(" ");
        int lastIndex = sList.length-1;

        return sList[lastIndex].length();
    }
}