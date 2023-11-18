//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	int findMinIndex(int coins[], int M, int V) {
	    for(int i = M; i > 0; i--) {
	        if(V < coins[i - 1]) continue;
	        return i - 1;
	    }
	    return -1;
	}
	public:
	int minCoins(int coins[], int M, int V) 
	{ 
	    // Your code goes here
	    sort(coins, coins + M);
	    int res = 0, index = findMinIndex(coins, M, V);
	    if(index == -1) return -1;
	    while(V >= coins[index]) {
	        V-= coins[index];
	        res++;
	    }
	    return (!V) ? res : -1;
	} 
	  
};

//{ Driver Code Starts.
int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
        int v, m;
        cin >> v >> m;

        int coins[m];
        for(int i = 0; i < m; i++)
        	cin >> coins[i];

      
	    Solution ob;
	    cout << ob.minCoins(coins, m, v) << "\n";
	     
    }
    return 0;
}

// } Driver Code Ends