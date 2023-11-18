#User function Template for python3
class Solution:
    def findMinIndex(self, coins: list[int], M: int, V: int) -> int:
        for i in range(M, 0, -1):
            if V < coins[i - 1]:
                continue
            return i - 1
        return -1
	def minCoins(self, coins, M, V):
		# code here
		coins.sort()
		res = 0
		index = self.findMinIndex(coins, M, V)
		while V >= coins[index]:
		    V -= coins[index]
		    res += 1
		return res if V == 0 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends