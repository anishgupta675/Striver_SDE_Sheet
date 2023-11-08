import java.util.*;

class Solution {

    public int trap(int[] height) {
        int ans = 0;
        int[] dp1 = new int[height.length];
        int[] dp2 = new int[height.length];
        dp1[0] = height[0];
        for(int i = 1; i < dp1.length; i++) dp1[i] = Math.max(dp1[i - 1], height[i]);
        dp2[height.length - 1] = height[height.length - 1];
        for(int i = dp2.length - 2; i >= 0; i--) dp2[i] = Math.max(dp2[i + 1], height[i]);
        for(int i = 0; i < height.length; i++) ans+= Math.min(dp1[i], dp2[i]) - height[i];
        return ans;
    }

    public static void main(String[] args) throws Exception {}
}