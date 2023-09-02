import java.util.*;

class Solution {

    private final int NO_OF_CHARS = 256;

    public int lengthOfLongestSubstring(String s) { 
        int i = 0, res = 0;
        int[] lastIndex = new int[NO_OF_CHARS];
        Arrays.fill(lastIndex, -1);
        for (int j = 0; j < s.length(); j++) {
            i = Math.max(i, lastIndex[s.charAt(j)] + 1);
            res = Math.max(res, j - i + 1);
            lastIndex[s.charAt(j)] = j;
        }
        return res;
    }

    public static void main(String[] args) throws Exception {}
}