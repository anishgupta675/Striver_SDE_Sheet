#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		res = []
		for i in range(0, 1 << N):
		    sum = 0
		    for j in range(N):
		        if (i & (1 << j)) != 0:
		            sum += arr[j]
		    res.append(sum)
		return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends