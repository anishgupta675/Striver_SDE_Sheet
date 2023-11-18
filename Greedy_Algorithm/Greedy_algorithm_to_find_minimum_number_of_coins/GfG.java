//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    int v = sc.nextInt();
                    int m = sc.nextInt();
                    int coins[] = new int[m];
                    for(int i = 0;i<m;i++)
                        coins[i] = sc.nextInt();
                    Solution ob = new Solution();
                    System.out.println(ob.minCoins(coins, m, v));
                }
        }
}    
// } Driver Code Ends


class Solution{
    
    private int findMinIndex(int[] coins, int M, int V) {
        for(int i = M; i > 0; i--) {
            if(V < coins[i - 1]) continue;
            return i - 1;
        }
        return -1;
    }

	public int minCoins(int coins[], int M, int V) 
	{ 
	    // Your code goes here
	    Arrays.sort(coins);
	    int res = 0, index = findMinIndex(coins, M, V);
	    while(V >= coins[index]) {
	        V-= coins[index];
	        res++;
	    }
	    return (V == 0) ? res : -1;
	} 
}