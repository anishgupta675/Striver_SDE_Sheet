#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        curr_sum, max_sum = 0, 0
        prefix_sum = {}
        for (i, curr) in enumerate(arr):
            curr_sum += curr
            if not curr_sum:
                max_sum = i + 1
            else:
                if curr_sum in prefix_sum:
                    max_sum = max(max_sum, i - prefix_sum[curr_sum])
                else:
                    prefix_sum[curr_sum] = i
        return max_sum
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends