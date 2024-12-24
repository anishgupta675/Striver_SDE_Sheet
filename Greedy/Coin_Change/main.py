#User function Template for python3
class Solution:
    def minCoinsRecur(self, i: int, total: int, coins: list):
        if not total:
            return 0
            if total < 0 or i == len(coins):
                return float('inf')
            take = float('inf')
            if coins[i] > 0:
                take = self.minCoinsRecur(i, total - coins[i], coins)
                if take != float('inf'):
                    take += 1
            no_take = self.minCoinsRecur(i + 1, total, coins)
            return min(take, no_take)

	def minCoins(self, coins, sum):
		# code here
		ans = self.minCoinsRecur(0, sum, coins)
		return ans if ans != float('inf') else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends
